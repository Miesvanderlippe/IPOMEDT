from classes.cart import Cart
import RPi.GPIO as GPIO
import time


class SearchAndDestroy:

    def __init__(self):
        self.cart = Cart()
        self.max_scan_distance = 70.0
        self.cart.start_sirene()

    def run(self):
        self.loop()

    def loop(self):

        prev_distance = 0

        while True:
            distance = self.poll_dis_reliable()

            # probably hit a wall.
            if round(distance) == round(prev_distance) and distance < 10:
                self.turret()
                print("MUUR!")

            prev_distance = distance
            print(distance)

            if self.max_scan_distance > distance > 10:

                if not self.cart.siren_running:
                    self.cart.start_sirene()

                if distance > (self.max_scan_distance / 2):
                    self.cart.forward(30)
                else:
                    self.cart.forward(20)
                time.sleep(0.1)
                self.cart.stop()

            else:
                if self.cart.siren_running:
                    self.cart.stop_sirene()

                if self.home() is None:
                    self.turret()

    def turret(self):
        distance = self.poll_dis_reliable()

        while distance > self.max_scan_distance or distance < 10:
            self.cart.turn_right_tick(1)
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

        distance = self.poll_dis()
        print(distance)

        if 1 < distance < self.max_scan_distance:
            return distance

        for i in range(5, 15):
            time.sleep(0.1)
            direction = self.cart.prev_turn != 'right'

            if direction:
                self.cart.turn_right_tick(i * 0.7, 22)
            else:
                self.cart.turn_left_tick(i * 0.7, 22)

            distance = self.poll_dis()
            print(distance)

            if 1 < distance < self.max_scan_distance:
                return distance

        while True:
            time.sleep(0.1)
            distance = self.poll_dis()
            if 1 < distance < self.max_scan_distance:
                return distance
            self.cart.turn_left_tick(1)

        return None


def main() -> None:

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    bot = SearchAndDestroy()
    bot.run()

if __name__ == "__main__":
    main()
