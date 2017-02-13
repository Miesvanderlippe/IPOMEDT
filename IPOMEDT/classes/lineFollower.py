import RPi.GPIO as GPIO
import time


class LineFollower:
    def __init__(self, pin: int):
        """
        Constructor voor de linefollower (zwart / wit) sensor
        :param pin: Pin waaraan de linefollower sensor zit
        """
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)

    def poll(self) -> bool:
        """
        Kijkt of de ondergrond zwart of wit is. De sensor geeft hier high (1)
        of low (0) voor terug. Omdat de pin op GPIO.IN staat kan je de status
        van de pin lezen.
        :return: Bool zwart of wit.
        """
        return GPIO.input(self.pin) == 0


def main() -> None:
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    sensor = LineFollower(25)

    # leest de sensor 100 keer uit met 1/10e seconde ertussen.
    for i in range(0, 100):
        print(sensor.poll())
        time.sleep(0.1)

if __name__ == '__main__':
    main()