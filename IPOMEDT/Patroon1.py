# classes importeren.
from classes.motor import Motor
from classes.lineFollower import LineFollower
from classes.ultraSonic import UltraSonic
from util.GPIOFuckUp import GPIOFuckUp
from RPi import GPIO
import time


# Hieronder variabelen
def main() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    testmotor1 = Motor([9, 10])
    testmotor2 = Motor([7, 8])
    linefollower = LineFollower(25)
    ultrasonic = UltraSonic([17, 18])
    boolean = False  # gaat standaart naar rechts draien

    try:
        while True:
            distance = ultrasonic.poll()
            if linefollower.poll() is True and distance > 11:  # true als de onder sensor op zwarte opevlakte rijd en de boven sensor geen opstake heeft gevonden
                print("Auto rijd op zwart")
                testmotor1.forward(15)
                testmotor2.forward(15)
            elif distance < 10 & boolean is True:  # als de afstand kleiner is dan 10 centimeter en de boolean waar is voer de onderstande code uit
                print("Afremen")
                testmotor1.stop()
                testmotor2.stop()
                testmotor2.forward(15)  # rechter wiel gaat naar links
                boolean is True
            elif distance < 10 & boolean is False:  # als de afstand kleiner is dan 10 centimeter en de boolean is niet waar is voer de onderstande code uit
                print("Afremen")
                testmotor1.stop()
                testmotor2.stop()
                testmotor1.forward(15)  # linker wiel gaat naar rechts
                boolean is False
            elif linefollower.poll() is True:  # False Als onder de auto de sensor white oppervlakte heeft gedectecteert
                print("Auto rijd op wit")
                testmotor1.stop()
                testmotor2.stop()

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    GPIOFuckUp()
    main()
