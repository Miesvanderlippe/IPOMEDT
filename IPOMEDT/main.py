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
    # terwel de auto rijde op een zwarte stip voer de onderstande code uit:
    try:
        while linefollower.poll() is True:
            print("Auto rijd op zwart")
            testmotor1.forward()
            testmotor2.forward()
            # terwel de afstandsmeter een obstakel heeft gedectecteerd van 10 <  centimeter of kleiner
            while ultrasonic.poll() < 11:
                # Mischien is afremmen onodig
                print("Afremen")
                testmotor1.stop()
                testmotor2.stop()
                # de robot gaat naar links
                print("draai 90 grade naar links")
                testmotor1.forward(10)
                testmotor2.backwards(20)
                time.sleep(0.5)
                links = 1
                # Als de afstandmeter een obstakel heeft gedecteerd na het draien naar links
                if links == 1 & ultrasonic.poll() < 11:
                    print("opstakel  gedecteerd")
                    print("draai 180 grade naar rechts")
                    testmotor2.forward(10)
                    testmotor1.backward(20)
                    time.sleep(1.0)

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
