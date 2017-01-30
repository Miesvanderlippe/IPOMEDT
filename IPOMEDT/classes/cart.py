import RPi.GPIO as GPIO
import time

if __name__ == "__main__":
    from motor import Motor
else:
    from classes.motor import Motor


class Cart:

    def __init__(self):
        self.l_wheel = Motor([9, 10])
        self.r_wheel = Motor([7, 8])

    def turn_right(self, speed, ratio):
        if ratio > 0:
            self.l_wheel.forward(speed * ratio)
            self.r_wheel.forward(speed)
        else:
            self.l_wheel.backward(speed * (ratio * -1))
            self.r_wheel.forward(speed)

    def turn_left(self, speed, ratio):
        if ratio > 0:
            self.r_wheel.forward(speed * ratio)
            self.l_wheel.forward(speed)
        else:
            self.r_wheel.backward(speed * (ratio * -1))
            self.l_wheel.forward(speed)

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

    cart.forward(12)
    time.sleep(0.7)

    cart.backward(12)
    time.sleep(0.7)

    cart.turn_left(17, -0.6)
    time.sleep(0.9)

    cart.turn_right(17, -0.6)
    time.sleep(0.9)

    cart.stop()

if __name__ == "__main__":
    main()
