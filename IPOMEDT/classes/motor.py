import RPi.GPIO as GPIO
import time


class Motor:

    def __init__(self, pins: list):

        GPIO.setup(pins[0], GPIO.OUT)
        GPIO.setup(pins[1], GPIO.OUT)

        self.pin1 = GPIO.PWM(pins[0], 30)
        self.pin2 = GPIO.PWM(pins[1], 30)

        self.pin1.start(0)
        self.pin2.start(0)

    def forward(self, speed: int = 100):
        self.pin1.ChangeDutyCycle(0)
        self.pin2.ChangeDutyCycle(speed)

    def backward(self, speed: int = 100):
        self.pin1.ChangeDutyCycle(speed)
        self.pin2.ChangeDutyCycle(0)

    def stop(self):
        self.pin1.ChangeDutyCycle(0)
        self.pin2.ChangeDutyCycle(0)


def main() -> None:

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    testmotor1 = Motor([9, 10])
    testmotor2 = Motor([7, 8])

    testmotor1.forward(30)
    time.sleep(0)

    testmotor1.backward(30)
    time.sleep(0)

    testmotor1.stop()

    testmotor2.forward(30)
    time.sleep(0)

    testmotor2.backward(30)
    time.sleep(0)

    testmotor2.stop()


if __name__ == '__main__':
    main()