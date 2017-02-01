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
        self.rechterwiel.backward(speed)

    def linksaf (self, speed):
        # draai rechts
        self.linkerwiel.backward(speed)
        self.rechterwiel.forward(speed)


def main() -> None:

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # initialiseer sonic en motor

    sensor = UltraSonic([17, 18])
    googleCar = GoogleCar()

    while True:
        # print(sensor.poll())
        print("Rijden.....")
        googleCar.linkerwiel.forward(20)
        googleCar.rechterwiel.forward(20)
        time.sleep(1)
        # googleCar.linkerwiel.stop()
        # googleCar.rechterwiel.stop()
        # time.sleep(0.2)

        if sensor.poll() > 6:
            randomCheck = random.choice([True, False])

            while randomCheck:
                randomRichting = random.choice([True, False])

                if randomRichting:
                    print("naar Links draaien")
                    googleCar.linksaf(50)
                    time.sleep(0.2)
                    if sensor.poll() > 6:
                        googleCar.linkerwiel.forward(20)
                        googleCar.rechterwiel.forward(20)
                        time.sleep(1)
                    else:
                        print("naar Rechts draaien")
                        googleCar.rechtsaf(50)
                        time.sleep(0.4)

                else:
                    print("naar Rechts draaien")
                    googleCar.rechtsaf(50)
                    time.sleep(0.2)
                    if sensor.poll() > 6:
                        googleCar.linkerwiel.forward(20)
                        googleCar.rechterwiel.forward(20)
                        time.sleep(1)
                    else:
                        print("naar Links draaien")
                        googleCar.linksaf(50)
                        time.sleep(0.4)
        else:
            googleCar.linkerwiel.backward(20)
            googleCar.rechterwiel.backward(20)
            time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
