import RPi.GPIO as GPIO
import time
from threading import Thread

if __name__ == "__main__":
    from motor import Motor
    from ultraSonic import UltraSonic
    from light import Light
else:
    from classes.motor import Motor
    from classes.ultraSonic import UltraSonic
    from classes.light import Light


class Cart:

    def __init__(self):
        self.l_wheel = Motor([9, 10])
        self.r_wheel = Motor([7, 8])
        self.l_light = Light(21)
        self.r_light = Light(20)
        self.ultrasonic = UltraSonic([17, 18])
        self.prev_turn = 'left'

        thread = Thread(target=self.siren_loop)
        thread.start()

    def turn_right(self, speed, ratio):
        self.prev_turn = 'right'
        if ratio > 0:
            self.l_wheel.forward(speed * ratio)
            self.r_wheel.forward(speed)
        else:
            self.l_wheel.backward(speed * (ratio * -1))
            self.r_wheel.forward(speed)

    def turn_left(self, speed, ratio):
        self.prev_turn = 'left'
        if ratio > 0:
            self.r_wheel.forward(speed * ratio)
            self.l_wheel.forward(speed)
        else:
            self.r_wheel.backward(speed * (ratio * -1))
            self.l_wheel.forward(speed)

    def turn_left_tick(self, ticks=1, speed=15, ratio=-1):
        self.turn_left(speed, ratio)
        time.sleep(0.1 * ticks)

    def turn_right_tick(self, ticks=1, speed=21, ratio=-1):
        self.turn_right(speed, ratio)
        time.sleep(0.06 * ticks)

    def stop(self):
        self.l_wheel.stop()
        self.r_wheel.stop()

    def forward(self, speed):
        self.r_wheel.forward(speed)
        self.l_wheel.forward(speed)

    def backward(self, speed):
        self.r_wheel.backward(speed)
        self.l_wheel.backward(speed)

    def siren_loop(self):
        while True:
            self.l_light.dim(100)
            self.r_light.dim(100)
            time.sleep(0.05)

            self.l_light.dim(0)
            self.r_light.dim(0)
            time.sleep(0.05)

            self.r_light.dim(100)
            time.sleep(0.05)

            self.r_light.dim(0)
            time.sleep(0.05)

            self.l_light.dim(100)
            time.sleep(0.05)

            self.l_light.dim(0)
            time.sleep(0.05)


def main() -> None:

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    cart = Cart()

    time.sleep(10)
    print("Twerkt dit?")
    time.sleep(10)
    print("'t werkt")

if __name__ == "__main__":
    main()
