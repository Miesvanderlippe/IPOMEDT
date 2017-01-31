import RPi.GPIO as GPIO
import time

if __name__ == "__main__":
    from motor import Motor
    from ultraSonic import UltraSonic
else:
    from classes.motor import Motor
    from classes.ultraSonic import UltraSonic


class Cart:

    def __init__(self):
        self.l_wheel = Motor([9, 10])
        self.r_wheel = Motor([7, 8])
        self.ultrasonic = UltraSonic([17, 18])
        self.prev_turn = 'left'

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


def main() -> None:

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    cart = Cart()

    cart.forward(20)
    time.sleep(0.7)

    cart.backward(20)
    time.sleep(0.7)

    cart.turn_left(20, 0.1)
    time.sleep(0.9)

    cart.turn_right(20, 0.1)
    time.sleep(0.9)

    cart.stop()

if __name__ == "__main__":
    main()
