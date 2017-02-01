import RPi.GPIO as GPIO
import time


class Motor:

    def __init__(self, pins: list):
        """
        Constructor voor de motor class.
        :param pins: Lijst met pins die motor gebruikt [1, 2]. Draait de motor
        verkeerd om? Wissel de pins om ([2, 1]).
        """

        # Pins opslaan om later aan te sturen
        self.pin1 = pins[0]
        self.pin2 = pins[1]

        # Pins instellen voor output (motoren vertellen geen verhaaltjes)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)

        # Pins op 0 zetten zodat ie niet onverwacht draait.
        GPIO.output(self.pin1, 0)
        GPIO.output(self.pin2, 0)

    def forward(self) -> None:
        """
        Doet de motor naar voren draaien. Hiervoor moet de eerste pin hoog
        staan.
        """
        GPIO.output(self.pin1, 1)
        GPIO.output(self.pin2, 0)

    def backward(self) -> None:
        """
        Doet de motor achteruit draaien. Hiervoor moet de tweede pin hoog
        staan.
        :return:
        """
        GPIO.output(self.pin1, 0)
        GPIO.output(self.pin2, 1)

    def stop(self) -> None:
        """
        Stopt de motor. Beide pins geven geen stroom.
        """
        GPIO.output(self.pin1, 0)
        GPIO.output(self.pin2, 0)


def main() -> None:
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # motoren aanmaken
    testmotor1 = Motor([10, 9])
    testmotor2 = Motor([8, 7])

    # motor 1 laten draaien (halve seconde)
    testmotor1.forward()
    time.sleep(0.5)

    # motor 1 achterwaards laten draaien (halve seconde)
    testmotor1.backward()
    time.sleep(0.5)

    # motor 1 stoppen
    testmotor1.stop()

    # motor 2 laten draaien (halve seconde)
    testmotor2.forward()
    time.sleep(0.5)

    # motor 2 achterwaards laten draaien (halve seconde)
    testmotor2.backward()
    time.sleep(0.5)

    # motor 2 stoppen
    testmotor2.stop()

    # Laat de 2e motor heel snel trillen bij wijze van expiriment.
    # Voor wanneer je benieuwd ben hoe snel een motor kan trillen.
    for i in range(0, 50):
        testmotor2.forward()
        time.sleep(0.012)

        testmotor2.backward()
        time.sleep(0.012)

        # altijd de motor stoppen, anders blijft ie draaien wanneer je script
        # stopt
        testmotor2.stop()

if __name__ == '__main__':
    main()
