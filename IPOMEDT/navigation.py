import time
import RPi.GPIO as GPIO
from classes.light import Light
from classes.motor import Motor
from classes.carClass import CarClass
from classes.lineFollower import LineFollower


def main() -> None:

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)

    motor1 = Motor([9, 10])
    motor2 = Motor([7, 8])

    light1 = Light(20)
    light2 = Light(21)

    lineFollow = LineFollower(25)
    carClass = CarClass()

    try:
        while True:
            time.sleep(0.2)
            carClass.light()
            if lineFollow.poll() is True:
                print("Black line")
                carClass.onBlack(75)
                light1.turn_on()
                light2.turn_on()
            else:
                print("not black line " + str(lineFollow.poll()))
                carClass.onWhite(75)

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
