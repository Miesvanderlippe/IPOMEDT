from classes.motor import Motor
from classes.lineFollower import LineFollower
from classes.ultraSonic import UltraSonic
import time


def main() -> None:
    testmotor1 = Motor([10, 9])
    testmotor2 = Motor([8, 7])
    linefollower = LineFollower(25)
    ultrasonic = UltraSonic([17, 18])

    while True:
        time.sleep(0.5)
        testmotor1.forward()
        if ultrasonic.poll() == 10:
            time.sleep(0.5)
            testmotor1.backward()
            testmotor2.backward()
        else:
            for i in range(0, 50):
                testmotor2.forward()
                time.sleep(0.012)

                testmotor2.backward()
                time.sleep(0.012)

                testmotor2.stop()

if __name__ == "__main__":
    main()
