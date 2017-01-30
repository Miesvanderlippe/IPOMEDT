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

        GPIO.output(self.trigger, False)

        wait = 0.5 - (timer() - self.last_poll)
        self.last_poll = timer()

        if wait > 0:
            time.sleep(wait)
            print("Waiting {0}".format(wait))

        # poll
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

        start_time = time.time()
        stop_time = start_time

        while GPIO.input(self.echo) == 0:
            start_time = time.time()

        while GPIO.input(self.echo) == 1:
            stop_time = time.time()

            if stop_time - start_time >= 0.04:
                retry = self.poll(depth - 1)

                if retry > 0:
                    return retry
                else:
                    return 1000

        elapsed_time = stop_time - start_time
        distance = elapsed_time * 34326

        return round(distance / 2, 3)

    def is_nearby(self, disance: float):
        return self.poll() < disance


def main() -> None:
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    sensor = UltraSonic([17, 18])

    for i in range(0, 100):
        print(sensor.poll())
        time.sleep(0.3)
        print(sensor.is_nearby(10))
        print(sensor.is_nearby(20))

if __name__ == '__main__':
    main()
