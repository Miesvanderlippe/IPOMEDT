if __name__ == '__main__':
    from sys import path

    path.append("..")

import RPi.GPIO as GPIO


class GPIOFuckUp:

    # noinspection PyBroadException
    def __init__(self):

        # Elke GPIO pin
        pins = [2, 3, 4, 5,
                6, 7, 8, 9,
                10, 11, 12,
                13, 14, 15,
                16, 17, 18,
                19, 20, 21,
                22, 23, 24,
                25, 26]

        # Loop door elke GPIO pin heen
        for pin in pins:
            # Probeer de GPIO pin of false te zetten.
            try:
                GPIO.output(pin, False)
            except RuntimeError:
                continue


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    GPIO.setmode(GPIO.BCM)
    GPIOFuckUp()


# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()