import RPi.GPIO as GPIO
import time


class Light:

    def __init__(self, pin: int):
        """
        Constructor voor een lampje.
        :param pin: Pin waar het lampje in geprikt zit.
        """
        GPIO.setup(pin, GPIO.OUT)
        self.pin = GPIO.PWM(pin, 1000)
        self.pin.start(0)

    def turn_on(self) -> None:
        """
        Zet het lampje op 100% felheid.
        """
        self.pin.ChangeDutyCycle(100)

    def turn_off(self) -> None:
        """
        Zet het lampje uit (0%)
        """
        self.pin.ChangeDutyCycle(0)

    def dim(self, percentage: int) -> None:
        """
        Dimt het lampje.
        :param percentage: 0-100 procent felheid.
        """
        self.pin.ChangeDutyCycle(percentage)


def main() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Maak de lampjes aan
    left_light = Light(26)
    right_light = Light(21)
    red_sirene = Light(20)
    blue_sirene = Light(16)

    # Alle lampjes uit
    left_light.turn_off()
    right_light.turn_off()
    red_sirene.turn_off()
    blue_sirene.turn_off()

    time.sleep(2)

    # Stuk voor stuk aan ( om na te kunnen kijken of de namen kloppen)
    left_light.turn_on()
    time.sleep(0.5)
    right_light.turn_on()
    time.sleep(0.5)
    red_sirene.turn_on()
    time.sleep(0.5)
    blue_sirene.turn_on()
    time.sleep(0.5)

    time.sleep(10)

    # Alle lampjes uit
    left_light.turn_off()
    right_light.turn_off()
    red_sirene.turn_off()
    blue_sirene.turn_off()

if __name__ == '__main__':
    main()
