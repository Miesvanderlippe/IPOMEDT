import RPi.GPIO as GPIO
import time
from timeit import default_timer as timer


class UltraSonic:

    def __init__(self, pins: list):

        self.trigger = pins[0]
        self.echo = pins[1]
        self.last_poll = timer()

        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def poll(self, depth=3):

        if depth < 1:
            return 0

        if depth < 3:
            print("retry")

        GPIO.output(self.trigger, False)

        wait = 0.0025 - (timer() - self.last_poll)
        self.last_poll = timer()

        if wait > 0:
            time.sleep(wait)

        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

        start_time = time.time()
        stop_time = start_time

        while GPIO.input(self.echo) == 0:
            start_time = time.time()

        while GPIO.input(self.echo) == 1:
            stop_time = time.time()

        elapsed_time = stop_time - start_time
        distance = elapsed_time * 34326

        if not distance > 1:
            retry = self.poll(depth - 1)

            if retry > 0:
                return retry
            else:
                return 1000

        return round(distance / 2, 3)

    def is_nearby(self, disance: float):
        return self.poll() < disance


def main() -> None:
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    sensor = UltraSonic([17, 18])

    while True:
        print(sensor.poll())

if __name__ == '__main__':
    main()
