from classes.motor import Motor
from classes.lineFollower import LineFollower
from classes.ultraSonic import UltraSonic
from RPi import GPIO
import time


def main() -> None:
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    testmotor1 = Motor([10, 9])
    testmotor2 = Motor([8, 7])
    linefollower = LineFollower(25)
    ultrasonic = UltraSonic([17, 18])

    # recht activeren gaat links
    # testmotor1.forward()

    # links activeren gaat rechter
    # testmotor2.forward()

    # wacht 0.1 seconden voordat hij begint met het uitvoeren van script
    time.sleep(0.1)

    while linefollower.poll():
        # terwel de auto rijde op een zwarte stip voer de onderstande code uit:
        testmotor1.forward()
        testmotor2.forward()
        # terwel de afstandsmeter een obstakel heeft gedectecteerd van 10 <  centimeter of kleiner
        while ultrasonic.poll() < 11:  # kleiner dan 10 centimeter
            # remmen stop de wilen met rijden
            testmotor1.stop()
            testmotor2.stop()
        else:
            testmotor1.forward()
            testmotor2.forward()
    # wat moet er gebeuren als er een witten stipje is gevonden
if __name__ == "__main__":
    main()