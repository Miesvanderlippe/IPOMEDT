if __name__ == "__main__":
    from sys import path
    path.append("..")

from classes.motor import Motor
from classes.lineFollower import LineFollower
from classes.ultraSonic import UltraSonic
from classes.light import Light
from util.GPIOFuckUp import GPIOFuckUp
from RPi import GPIO
import time


def main() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    testmotor1 = Motor([9,10])
    testmotor2 = Motor([7, 8])
    linefollower = LineFollower(25)
    ultrasonic = UltraSonic([17, 18])
    left_light = Light(21)
    right_light = Light(20)

    # sensor
    sensor = UltraSonic([17, 18])
    distance = sensor.poll()

    while True:
            distance = sensor.poll()
            if distance > 20 and linefollower.poll() is True:
                print("Afstand tot voorwerp", distance)
                testmotor1.forward(50)
                testmotor2.forward(50)
                left_light.turn_on()
                left_light.turn_off()
                right_light.turn_on()
                right_light.turn_off()
                time.sleep(1)
            elif distance < 5:
                print("Linksaf")
                testmotor1.forward(10)
                testmotor2.backward(30)
                left_light.turn_on()
                time.sleep(1)
            elif linefollower.poll() == False:
                print("U rijdt op wit, ga terug")
                testmotor1.backward(25)
                testmotor2.backward(25)
                left_light.turn_on()
                right_light.turn_on()
                time.sleep(1)
            elif distance < 20 and distance > 5:
                print("U nadert iets, rij langzamer")
                testmotor1.forward(20)
                testmotor2.forward(20)
                testmotor1.forward(10)
                testmotor2.forward(10)
                left_light.turn_on()
                right_light.turn_on()


if __name__ == "__main__":
    GPIOFuckUp()

    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()


