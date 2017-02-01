from classes.motor import Motor
from classes.lineFollower import LineFollower
from classes.ultraSonic import UltraSonic
from classes.light import Light
from RPi import GPIO
import time


def main() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    testmotor1 = Motor([9,10])
    testmotor2 = Motor([7, 8])
    linefollower = LineFollower(25)
    ultrasonic = UltraSonic([17, 18])

    # sensor
    sensor = UltraSonic([17, 18])
    distance = sensor.poll()

    while True:
        distance = sensor.poll()
        if distance > 50 and linefollower.poll() is False:
            print(distance)
            print("Afstand tot voorwerp")
            testmotor1.forward(20)
            testmotor2.forward(20)
            time.sleep(1)
        elif distance < 30:
            print("Linksaf")
            testmotor1.forward(20)
            testmotor2.backward(10)
        elif linefollower.poll() == True:
            print("U rijdt op wit, ga terug")
            testmotor1.forward(15)
            testmotor2.backward(5)
            time.sleep(1)







if __name__ == "__main__":
    main()


