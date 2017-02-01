from classes.motor import Motor
from classes.lineFollower import LineFollower
from classes.ultraSonic import UltraSonic
from classes.light import Light
from RPi import GPIO
import time


def main() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    testmotor1 = Motor([10,9])
    testmotor2 = Motor([8, 7])
    linefollower = LineFollower(25)
    ultrasonic = UltraSonic([17, 18])


    sensor = UltraSonic([17, 18])
    distance = sensor.poll()

    while True:
        distance = sensor.poll()
        if distance > 5:
            print(distance)
            print("Afstand tot voorwerp")
            testmotor1.forward(20)
            testmotor2.forward(20)
        else:
            print("Linksaf")
            testmotor1.forward(20)
            testmotor2.backward(10)


if __name__ == "__main__":
    main()


