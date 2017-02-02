from classes.cart import Cart
from timeit import default_timer as timer
import RPi.GPIO as GPIO
import time


class SearchAndDestroy:

    def __init__(self):
        self.cart = Cart()
        self.max_scan_distance = 70.0
        self.cart.start_sirene()
        self.previous_successful_turn = 'left'
        self.cart.turn_on_lights()

    def run(self):
        self.loop()

    def loop(self):

        prev_distance = 0
        time_start = timer()

        while True:
            distance = self.poll_dis_reliable()

            # probably hit a wall.
            if round(distance) == round(prev_distance) and distance < 10:
                print("This is probably a wall")
                self.cart.turn_off_lights()
                time.sleep(0.2)
                self.cart.turn_on_lights()
                self.cart.backward(40)
                time.sleep(0.2)
                self.cart.turn_right_tick(8)
                self.turret()

            if round(timer() - time_start, 1) % 0.5 == 0:
                prev_distance = distance
                print("setting prev distance")

            if self.max_scan_distance > distance > 10:

                if not self.cart.siren_running:
                    self.cart.start_sirene()

                if distance > 90:
                    speed = 100
                else:
                    speed = distance + 10

                print("Chasing at speed {0}".format(speed))
                self.cart.forward(speed)

            else:
                if self.cart.siren_running:
                    self.cart.stop_sirene()

                if self.home() is None:
                    print("Homing failed")
                    self.turret()

    def turret(self):
        print("Turning")
        distance = self.poll_dis_reliable()

        while distance > self.max_scan_distance or distance < 10:
            self.cart.turn_right_tick(1.5, 23)

            distance = self.poll_dis_reliable()

        print("returning: {0}".format(distance))
        return distance

    def poll_dis(self):
        dist = self.cart.ultrasonic.poll()
        return dist if dist < 1000 else 0

    def poll_dis_reliable(self):
        polls = [
            self.poll_dis(),
            self.poll_dis(),
            self.poll_dis(),
            self.poll_dis(),
            self.poll_dis(),
        ]

        return sum(polls) / len(polls)

    def home(self):
        print("Homing")
        distance = self.poll_dis()
        print(distance)

        if 1 < distance < self.max_scan_distance:
            return distance

        self.cart.prev_turn = self.previous_successful_turn

        for i in range(1, 10):

            direction = self.cart.prev_turn != 'right'

            if direction:
                self.cart.turn_right_tick(i * 1.8, 23)
            else:
                self.cart.turn_left_tick(i * 1.8, 23)

            distance = self.poll_dis_reliable()

            if 1 < distance < self.max_scan_distance:
                return distance

        return None


def main() -> None:

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    bot = SearchAndDestroy()
    bot.run()

if __name__ == "__main__":
    main()
