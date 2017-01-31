from classes.motor import Motor
from classes.lineFollower import LineFollower
from classes.ultraSonic import UltraSonic
import time
from RPi import GPIO


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

    while LineFollower.poll():
        # bij het begin van de script ga naar voor
        testmotor1.forward()
        testmotor2.forward()
        # Als er een obstekel gedectecteerd wordt
        if ultrasonic.poll() == 10:  # 10 centimeter
            # Voer de volgende uit

            # remmen Stop de wilen met rijden
            testmotor1.stop()
            testmotor2.stop()

            time.sleep(0.5)
            # Ga naar Achter
            testmotor1.backward()
            testmotor2.backward()
            time.sleep(0.5)

        else:
            # wat moet er gebeuren als geen opstakel is
            for i in range(0, 50):
                testmotor2.forward()
                time.sleep(0.012)

                testmotor2.backward()
                time.sleep(0.012)

                testmotor2.stop()

if __name__ == "__main__":
    main()
