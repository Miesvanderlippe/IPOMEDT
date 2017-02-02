from classes.cart import Cart
from timeit import default_timer as timer
import RPi.GPIO as GPIO
import time


class SearchAndDestroy:

    def __init__(self):
        """
        Sets up the Search and 'destroy' class.
        """
        self.cart = Cart()
        self.max_scan_distance = 100.0
        self.cart.start_sirene()
        self.previous_successful_turn = 'left'
        self.cart.turn_on_lights()

    def run(self) -> None:
        """
        Starts the program
        """
        self.loop()

    def loop(self) -> None:
        """
        Runs the loop that should catch criminals.
        """
        prev_distance = 0
        time_start = timer()

        while True:
            distance = self.poll_dis_reliable()

            # probably hit a wall.
            if round(distance) == round(prev_distance) and distance < 10:

                time.sleep(0.5)

                # wait a bit and check again.
                if round(distance) != round(self.poll_dis_reliable()):
                    continue

                print("This is probably a wall")

                # Move backwards a bit, turn around. Run scan.
                self.cart.backward(40)
                time.sleep(0.2)
                self.cart.turn_right_tick(8)
                self.turret()

            # update distance every so often.
            if round(timer() - time_start, 1) % 0.2 == 0:
                prev_distance = distance
                print("setting prev distance")

            # chase if close enough, and not too close.
            if self.max_scan_distance > distance > 5:

                # proper chases require proper equipment.
                if not self.cart.siren_running:
                    self.cart.start_sirene()

                # drive faster if further away from suspect
                if distance > 90:
                    speed = 100
                else:
                    speed = (distance / 2) + 10

                print("Chasing at speed {0}".format(speed))
                self.cart.forward(speed)

            # we lost them boys
            else:
                if self.cart.siren_running:
                    self.cart.stop_sirene()

                # try looking in front of ourselves.
                if self.home() is None:
                    print("Homing failed")
                    self.turret()

    def turret(self) -> float:
        """
        Spins the bot slowly, looking for nearby objects.
        Loops until found.
        :return: distance with 2 decimal precision.
        """
        print("Turning")
        distance = self.poll_dis_reliable()

        while distance > self.max_scan_distance or distance < 10:
            self.cart.turn_right_tick(1.5, 23)

            distance = self.poll_dis_reliable()

        print("returning: {0}".format(distance))
        return distance

    def poll_dis(self) -> float:
        """
        Poll the ultrasonic sensor.
        :return: Distance with 2 decimals precision.
        """
        dist = self.cart.ultrasonic.poll()
        return dist if dist < 1000 else 0

    def poll_dis_reliable(self) -> float:
        """
        Polls the distance sensor 5 times, returns the average.
        :return: Distance with 2 deicmals precission.
        """
        polls = [
            self.poll_dis(),
            self.poll_dis(),
            self.poll_dis(),
            self.poll_dis(),
            self.poll_dis(),
        ]

        return round(sum(polls) / len(polls), 2)

    def home(self) -> float:
        """
        Look in front of the robot for nearby enough objects. Gives up after
        scanning ~200 degrees
        :return: distance to object in 2 decimals precision
        """
        print("Homing")
        distance = self.poll_dis()
        print(distance)

        if 1 < distance < self.max_scan_distance:
            return distance

        # first look in last succesful direction. If we're making a long left
        # there's no need to look right at first.
        if self.previous_successful_turn == 'right':
            self.cart.prev_turn = 'left'
        else:
            self.cart.prev_turn = 'right'

        # turn 1 step left, 2 right, 3 left etc. Scans center first, wider area
        # second.
        for i in range(2, 7):

            direction = self.cart.prev_turn != 'right'

            if direction:
                self.cart.turn_right_tick(i * 1, 33)
            else:
                self.cart.turn_left_tick(i * 1, 33)

            time.sleep(0.2)
            distance = self.poll_dis_reliable()

            if 1 < distance < self.max_scan_distance:
                return distance

        # didn't find them.
        return None


def main() -> None:

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    bot = SearchAndDestroy()
    bot.run()

if __name__ == "__main__":
    main()
