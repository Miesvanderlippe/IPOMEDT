import RPi.GPIO as GPIO
import time


class LineFollower:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)

    def poll(self):
        return GPIO.input(self.pin) == 0


def main() -> None:
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    sensor = LineFollower(25)

    for i in range(0, 100):
        print(sensor.poll())
        time.sleep(0.1)

if __name__ == '__main__':
    main()
