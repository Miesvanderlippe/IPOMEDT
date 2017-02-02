if __name__ == "__main__":
    from sys import path
    path.append("..")
# Hieronder worden alle classes geimporteerd.
from classes.motor import Motor
from classes.lineFollower import LineFollower
from classes.ultraSonic import UltraSonic
from classes.light import Light
from util.GPIOFuckUp import GPIOFuckUp
from RPi import GPIO
import time
# Hieronder benoem ik alle benodigde variabelen die ik gebruik.
def main() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    testmotor1 = Motor([9, 10])
    testmotor2 = Motor([7, 8])
    linefollower = LineFollower(25)
    ultrasonic = UltraSonic([17, 18])
    right_light = Light(21)
    left_light = Light(20)
    siren_blue = Light(16)
    siren_red = Light(26)
    """Hieronder maak ik een while statement die zich blijft herhalen en kijkt of er een muur dichtbij genoeg is, mocht dat het geval zijn
    dan maakt hij een bocht naar links en gaat hij weer verder. Als hij in het witte gedeelte komt dan rijdt hij een stukje naar achter maar
    de rechter wiel draait iets sneller waardoor hij weer recht op de baan terug komt"""
    # sensor
    sensor = UltraSonic([17, 18])
    try:
        while True:
                distance = ultrasonic.poll()
                time.sleep(0.1)
                if distance > 30 and  linefollower.poll() is True: # kijkt of de afstand tot de muur groter of gelijk aan de muur is en dat hij op het zwarte geelte zit.
                    print("Afstand tot voorwerp", distance)
                    testmotor1.stop() # stopt de auto
                    testmotor2.stop()
                    testmotor1.forward(40) #linker wiel
                    testmotor2.forward(40) #rechter wiel
                    left_light.turn_on() # zet de lichten aan
                    right_light.turn_on()
                    siren_red.turn_on() # zet de sirene aan.
                    siren_blue.turn_on()

                elif linefollower.poll() is False:  # hij kijkt of hij op het witte is als dat waar is rijdt hij een stuk terug.
                    print("U rijdt op wit, ga terug")
                    testmotor1.stop()
                    testmotor2.stop()
                    testmotor1.backward(10)  # linker wiel
                    testmotor2.forward(20)  # rechter wiel
                    left_light.turn_on()
                    right_light.turn_on()
                    siren_blue.turn_on()
                    siren_red.turn_on()

                elif distance < 40 and distance > 25:  # hij kijkt of de afstand tot de muur tussen de 15 en 40 cm is, zo ja dan rijdt hij iets langzamer
                    print("U nadert iets, rij langzamer: ", distance )
                    testmotor1.stop()
                    testmotor2.stop()
                    testmotor1.forward(35)
                    testmotor2.forward(35)
                    testmotor1.forward(25)
                    testmotor2.forward(25)
                    left_light.turn_on()
                    right_light.turn_on()
                    siren_red.turn_on()
                    siren_blue.turn_on()
                    time.sleep(0.1)

                elif distance < 30 and distance > 10 and linefollower.poll() is True:  # Kijkt of de afstand tot voorwerp kleiner is dan 25 en groter dan 10
                    print("Linksaf: ", distance)
                    testmotor1.stop()
                    testmotor2.stop()
                    testmotor1.forward(0)  # linker wiel
                    testmotor2.forward(26)  # rechter wiel
                    right_light.turn_on()
                    siren_blue.turn_on()
                    time.sleep(1.2)

                elif distance > 8 or distance < 10 and linefollower.poll() is True:  # Als hij te dicht bij de muur komt, corrigeert hij zich door 1 wiel iets harder te laten gaan
                    print ("Muur dichtbij, bijsturen!")
                    testmotor1.stop()  # stopt de auto
                    testmotor2.stop()
                    testmotor1.forward(40)  # r wiel
                    testmotor2.forward(37)  # l wiel
                    left_light.turn_on()  # zet de lichten aan
                    right_light.turn_on()
                    siren_red.turn_on()  # zet de sirene aan.
                    siren_blue.turn_on()


                else:
                    print("De motor stopt")
                    testmotor1.stop()
                    testmotor2.stop()
                    time.sleep(2.5)




    except KeyboardInterrupt:
        GPIO.cleanup()
    testmotor1.stop()
    testmotor2.stop()


if __name__ == "__main__":
    GPIOFuckUp()
    main()
