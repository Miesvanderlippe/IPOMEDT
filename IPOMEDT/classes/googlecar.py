import RPi.GPIO as GPIO # Import the GPIO Library import time # Import the Time library
from ultraSonic import UltraSonic
from motor import Motor
from light import Light
import time
import random


class GoogleCar:

    def __init__(self):
        self.linkerwiel = Motor([9, 10])
        self.rechterwiel = Motor([7, 8])
        self.right_light = Light(21)
        self.left_light = Light(20)
        self.siren_blue = Light(16)
        self.siren_red = Light(26)

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

    googleCar.siren_blue.turn_on()
    googleCar.siren_red.turn_on()
    googleCar.linkerwiel.stop()
    googleCar.rechterwiel.stop()
    while True:
        # print(sensor.poll())
        if sensor.poll() > 6:

            randomRichting = random.choice([1, 2, 3])

            if randomRichting == 1:
                print("naar Links draaien")
                googleCar.left_light.turn_on()
                googleCar.linksaf(50)
                time.sleep(0.2)
                googleCar.left_light.turn_off()
                if sensor.poll() > 6:
                    print("Rijden.....")
                    googleCar.left_light.turn_on()
                    googleCar.right_light.turn_on()
                    googleCar.linkerwiel.forward(20)
                    googleCar.rechterwiel.forward(20)
                    time.sleep(1)
                    googleCar.left_light.turn_off()
                    googleCar.right_light.turn_off()
                else:
                    print("naar Rechts draaien")
                    googleCar.right_light.turn_on()
                    googleCar.rechtsaf(50)
                    time.sleep(0.4)
                    googleCar.right_light.turn_off()

            elif randomRichting == 2:
                print("naar Rechts draaien")
                googleCar.rechtsaf(50)
                googleCar.right_light.turn_on()
                time.sleep(0.2)
                googleCar.left_light.turn_off()
                if sensor.poll() > 6:
                    print("Rijden.....")
                    googleCar.left_light.turn_on()
                    googleCar.right_light.turn_on()
                    googleCar.linkerwiel.forward(20)
                    googleCar.rechterwiel.forward(20)
                    time.sleep(1)
                    googleCar.left_light.turn_off()
                    googleCar.right_light.turn_off()
                else:
                    print("naar Links draaien")
                    googleCar.left_light.turn_on()
                    googleCar.linksaf(50)
                    time.sleep(0.4)
                    googleCar.left_light.turn_off()
            elif randomRichting == 3:
                if sensor.poll() > 6:
                    print("Rijden.....")
                    googleCar.left_light.turn_on()
                    googleCar.right_light.turn_on()
                    googleCar.linkerwiel.forward(20)
                    googleCar.rechterwiel.forward(20)
                    time.sleep(1)
                    googleCar.left_light.turn_off()
                    googleCar.right_light.turn_off()
                else:
                    print("Achteruit rijden")
                    googleCar.linkerwiel.backward(20)
                    googleCar.rechterwiel.backward(20)
                    time.sleep(1)
        else:
            print("Achteruit rijden")
            googleCar.linkerwiel.backward(20)
            googleCar.rechterwiel.backward(20)
            time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
