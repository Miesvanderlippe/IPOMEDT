import RPi.GPIO as GPIO
import time


class Motor:

    def __init__(self, pins: list):

        self.pin1 = pins[0]
        self.pin2 = pins[1]

        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)

        GPIO.output(self.pin1, 0)
        GPIO.output(self.pin2, 0)

    def forward(self):
        GPIO.output(self.pin1, 1)
        GPIO.output(self.pin2, 0)

    def backward(self):
        GPIO.output(self.pin1, 0)
        GPIO.output(self.pin2, 1)

    def stop(self):
        GPIO.output(self.pin1, 0)
        GPIO.output(self.pin2, 0)


def main() -> None:
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    testmotor1 = Motor([10, 9])
    testmotor2 = Motor([8, 7])

    testmotor1.forward()
    time.sleep(0.5)

    testmotor1.backward()
    time.sleep(0.5)

    testmotor1.stop()

    testmotor2.forward()
    time.sleep(0.5)

    testmotor2.backward()
    time.sleep(0.5)

    testmotor2.stop()

    for i in range(0, 50):
        testmotor2.forward()
        time.sleep(0.012)

        testmotor2.backward()
        time.sleep(0.012)

        testmotor2.stop()

if __name__ == '__main__':
    main()
