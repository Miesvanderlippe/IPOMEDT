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
    swich = False  # gaat standaart naar rechts draien
    teller = 0

    try:
        while True:
            distance = ultrasonic.poll()
            lightsensor = linefollower.poll()
            time.sleep(0.1)
            if lightsensor is True and distance > 30:  # true als de onder sensor op zwarte opevlakte rijd en de boven sensor geen opstake heeft gevonden
                print("Auto rijd op zwart. afstand",distance)
                testmotor1.forward(50)
                testmotor2.forward(50)

            elif lightsensor is True and distance < 30 and swich is False and teller < 5:  # hij kijkt of hij op het witte is als dat waar is rijdt hij een stuk terug.
                print("rechts", distance,teller)
                testmotor1.stop()
                testmotor2.stop()
                testmotor1.backward(50)  # linker wiel
                testmotor2.forward(40)  # rechter wiel
                time.sleep(3.5)
                swich = True
                teller += 1

            elif lightsensor is True and distance < 30 and swich is True and teller < 5:
                print("links", distance, teller)
                testmotor1.stop()
                testmotor2.stop()
                testmotor2.backward(50)
                testmotor1.forward(40)
                time.sleep(1.5)
                swich = False
                teller += 1

            elif teller == 5:
                print("achteruit Let: op !")
                testmotor1.stop()
                testmotor2.stop()
                testmotor1.backward(50)
                testmotor2.backward(50)
                time.sleep(1.5)

            elif lightsensor is False:
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