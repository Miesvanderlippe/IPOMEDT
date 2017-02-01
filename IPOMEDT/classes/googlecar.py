import RPi.GPIO as GPIO # Import the GPIO Library import time # Import the Time library
from ultraSonic import UltraSonic
from motor import Motor
import time
import random


class GoogleCar:

    def __init__(self):
        self.linkerwiel = Motor([9, 10])
        self.rechterwiel = Motor([7, 8])

    def rechtsaf (self, speed):
        # draai rechts
        self.linkerwiel.forward(speed)
        # self.rechterwiel.backward(speed)

    def linksaf (self, speed):
        # draai rechts
        # self.linkerwiel.backward(speed)
        self.rechterwiel.forward(speed)


def main() -> None:

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # initialiseer sonic en motor

    sensor = UltraSonic([17, 18])
    googleCar = GoogleCar()

    while True:
        # print(sensor.poll())

        while sensor.poll() < 6:
            randomRichting = random.choice([True, False])



            if randomRichting:
                googleCar.linksaf(50)
                time.sleep(0.2)
                if sensor.poll() > 6:
                    googleCar.linkerwiel.forward(20)
                    googleCar.rechterwiel.forward(20)
                    time.sleep(1)
                else:
                    googleCar.rechtsaf(50)
                    time.sleep(0.4)

            else:
                googleCar.rechtsaf(50)
                time.sleep(0.2)
                googleCar.linkerwiel.forward(20)
                googleCar.rechterwiel.forward(20)
                time.sleep(1)
                if sensor.poll() > 6:
                    googleCar.linkerwiel.forward(20)
                    googleCar.rechterwiel.forward(20)
                    time.sleep(1)
                else:
                    googleCar.linksaf(50)
                    time.sleep(0.4)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterupt:
        GPIO.cleanup()
