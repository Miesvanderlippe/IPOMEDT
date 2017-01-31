from classes.ultraSonic import UltraSonic
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

        while True:
            distance = self.poll_dis()
            print(distance)

            if distance < self.max_scan_distance and distance > 10:

                if not self.cart.siren_running:
                    self.cart.start_sirene()

                # self.cart.forward(40)
                time.sleep(0.2)
                self.cart.stop()

            else:
                if self.cart.siren_running:
                    self.cart.stop_sirene()

                self.home()

    def poll_dis(self):
        dist = self.cart.ultrasonic.poll()
        return dist if dist < 1000 else 0

    def home(self):

        distance = self.poll_dis()
        print(distance)

        if 1 < distance < self.max_scan_distance:
            return distance

        for i in range(0, 12):
            time.sleep(0.1)
            direction = self.cart.prev_turn != 'right'

            if direction:
                self.cart.turn_right_tick(i)
            else:
                self.cart.turn_left_tick(i)

            time.sleep(0.1)
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


def main() -> None:

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    bot = SearchAndDestroy()
    bot.run()

if __name__ == "__main__":
    main()
