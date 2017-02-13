# classes importeren.
from classes.motor import Motor
from classes.lineFollower import LineFollower
from classes.ultraSonic import UltraSonic
from util.GPIOFuckUp import GPIOFuckUp
from RPi import GPIO
import time
from classes.light import Light


# Hieronder variabelen
def main() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    testmotor1 = Motor([9, 10])
    testmotor2 = Motor([7, 8])
    linefollower = LineFollower(25)
    ultrasonic = UltraSonic([17, 18])
    swich = False  # gaat standaart naar rechts draien
    right_light = Light(21) #  Rechter led voorkant
    left_light = Light(13) #  Linker led voorkant
    siren_blue = Light(5) #  Links led achterkant

    try:
        while True:
            distance = ultrasonic.poll()
            lightsensor = linefollower.poll()
            time.sleep(0.1)
            if lightsensor is False and distance > 30:  # true als de onder sensor op zwarte opevlakte rijd en de boven sensor geen opstake heeft gevonden
                print("Auto rijd op zwart. afstand",distance)
                testmotor1.forward(100)
                testmotor2.forward(100)
                left_light.turn_on()  #  zet de linker led aan
                right_light.turn_on()  #  zet de rechter led aan

            elif lightsensor is False and distance < 30 and swich is False:  # hij kijkt of hij op het witte is als dat waar is rijdt hij een stuk terug.
                print("rechts", distance)
                testmotor1.stop()
                testmotor2.stop()
                testmotor1.backward(50)  # linker wiel
                testmotor2.forward(20)  # rechter wiel
                time.sleep(1.5)
                swich = True

            elif lightsensor is False and distance < 30 and swich is True:
                print("links", distance)
                testmotor1.stop()
                testmotor2.stop()
                testmotor2.backward(100)
                testmotor1.backward(100)
                time.sleep(1.5)
                swich = False

            elif lightsensor is True:
                print("Auto rijd op wit", distance)
                print(distance)
                testmotor1.stop()
                testmotor2.stop()
                GPIO.cleanup()

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    GPIOFuckUp()
    main()