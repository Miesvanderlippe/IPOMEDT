import RPi.GPIO as GPIO
import time


class Motor:

    def __init__(self, pins: list):
        """
        Constructor voor de motor class.
        :param pins: Lijst met pins die motor gebruikt [1, 2]. Draait de motor
        verkeerd om? Wissel de pins om ([2, 1]).
        """

        # Pins instellen voor output (motoren vertellen geen verhaaltjes)
        GPIO.setup(pins[0], GPIO.OUT)
        GPIO.setup(pins[1], GPIO.OUT)

        # Pins opslaan om later aan te sturen
        self.pin1 = GPIO.PWM(pins[0], 30)
        self.pin2 = GPIO.PWM(pins[1], 30)

        # Pins op 0 zetten zodat ie niet onverwacht draait.
        self.pin1.start(0)
        self.pin2.start(0)

    def forward(self, speed: int = 100):
        """
        Doet de motor naar voren draaien. Hiervoor moet de eerste pin hoog
        staan.
        """
        self.pin1.ChangeDutyCycle(0)
        self.pin2.ChangeDutyCycle(speed)

    def backward(self, speed: int = 100):
        """
        Doet de motor achteruit draaien. Hiervoor moet de tweede pin hoog
        staan.
        """
        self.pin1.ChangeDutyCycle(speed)
        self.pin2.ChangeDutyCycle(0)

    def stop(self):
        """
        Stopt de motor. Beide pins geven geen stroom.
        """
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

    # motor 1 stoppen
    testmotor1.stop()

    testmotor2.forward(30)
    time.sleep(0)

    testmotor2.backward(30)
    time.sleep(0)

    # motor 2 stoppen
    testmotor2.stop()

if __name__ == '__main__':
    main()