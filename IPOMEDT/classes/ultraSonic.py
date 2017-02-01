import RPi.GPIO as GPIO
import time


class UltraSonic:
    def __init__(self, pins: list):
        """
        Constructor voor de nabijheidssensor
        :param pins: lijst met pins die de sensor gebruikt [trigger, echo]
        """
        self.trigger = pins[0]
        self.echo = pins[1]

        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def poll(self) -> float:
        """
        Kijkt hoever de sensor bij iets vandaan is.
        Niet te snel achter elkaar aanroepen, dit geeft inaccurate gegevens.
        :return: Afstand met 2 punten precisie.
        """
        GPIO.output(self.trigger, False)

        # poll - geeft het signaal aan de sensor om te meten.
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
                stop_time = start_time
                break

        # De tijd die het gekost heeft voor de sensor om van high naar low
        # te gaan is de tijd die het duurde voor het geluid om terug te keren
        # duur * geluidssnelheid = afstand. Rekenkunde enzo.
        elapsed_time = stop_time - start_time
        distance = elapsed_time * 34326

        return round(distance / 2, 3)


def main() -> None:
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    sensor = UltraSonic([17, 18])

    for i in range(0, 100):
        print(sensor.poll())
        time.sleep(0.1)


if __name__ == '__main__':
    main()
