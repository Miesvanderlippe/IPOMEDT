from classes.motor import Motor
from classes.lineFollower import LineFollower
from classes.ultraSonic import UltraSonic
from classes.light import Light
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


    sensor = UltraSonic([17, 18])
    distance = sensor.poll()

    while True:
        distance = sensor.poll()
        if distance > 15:
            testmotor1.forward()
            testmotor2.forward()
            time.sleep(0.5)
            testmotor1.stop()
            testmotor2.stop()
        else:
            testmotor1.forward()
            testmotor2.backward()
            time.sleep(0.5)
            testmotor1.stop()
            testmotor2.stop()

if __name__ == "__main__":
    main()

