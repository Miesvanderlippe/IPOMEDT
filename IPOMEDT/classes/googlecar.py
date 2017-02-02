import RPi.GPIO as GPIO  # Import the GPIO Library import time # Import the Time library
from ultraSonic import UltraSonic
from motor import Motor
from light import Light
from time import sleep
from random import randint
from timeit import default_timer as timer


class GoogleCar:
    def __init__(self):  # Nieuwe motoren en lichtjes aanmaken uit de Motor en Light Class
        self.linkerwiel = Motor([9, 10])
        self.rechterwiel = Motor([7, 8])
        self.right_light = Light(21)
        self.left_light = Light(20)
        self.siren_blue = Light(16)
        self.siren_red = Light(26)
        self.sensor = UltraSonic([17, 18])

    def rechtsaf(self, speed):  # draai rechts
        self.linkerwiel.forward(speed)
        self.rechterwiel.backward(speed)

    def linksaf(self, speed):  # draai rechts
        self.linkerwiel.backward(speed)
        self.rechterwiel.forward(speed)

    def vooruit(self, speed):  # vooruit rijden
        self.linkerwiel.forward(speed)
        self.rechterwiel.forward(speed)

    def achteruit(self, speed):  # achteruit rijden
        self.linkerwiel.backward(speed)
        self.rechterwiel.backward(speed)

    def afstand_gem(self):
        afstands_lijst = [self.sensor.poll(),
                  self.sensor.poll(),
                  self.sensor.poll(),
                  self.sensor.poll(),
                  self.sensor.poll()]

        return sum(afstands_lijst) / len(afstands_lijst)


def main() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # initialiseer afstandsmeten en motor
    sensor = UltraSonic([17, 18])
    googleCar = GoogleCar()

    last_richting = 0  # laatste richting bijhouden

    while True:
        # sirene lampjes altijd aan houden
        googleCar.siren_blue.turn_on()
        googleCar.siren_red.turn_on()

        if sensor.poll() > 7:  # alleen uitvoeren als de bot niet te dicht bij de obstakels is
            print(googleCar.afstand_gem())
            randomRichting = randint(0, 2)  # kies een willekeurige richting
            start = timer()

            if randomRichting == 0 and last_richting == 0:  # richting links
                print("naar Links draaien")
                googleCar.left_light.turn_on()
                googleCar.linksaf(50)
                sleep(0.2)
                googleCar.left_light.turn_off()
                last_richting = 1

            elif randomRichting == 1 and last_richting == 1:  # richting rechts
                print("naar Rechts draaien")
                googleCar.rechtsaf(50)
                googleCar.right_light.turn_on()
                sleep(0.2)
                googleCar.right_light.turn_off()
                last_richting = 0

            elif randomRichting == 2:  # rechtdoorgaan
                print("Rechtdoor rijden")
                while googleCar.afstand_gem() > 7 and timer() - start < 0.5:
                    googleCar.vooruit(20)  # alleen vooruit als het kan.


            else:
                print("Rechtdoor rijden")
                while googleCar.afstand_gem() > 7 and timer() - start < 0.5:
                    googleCar.vooruit(20)  # alleen vooruit als het kan.

        else:
            print("Achteruit rijden")
            googleCar.achteruit(20)
            sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()  # opschonen van de pins
