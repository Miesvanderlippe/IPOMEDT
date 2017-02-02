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

    timer_left = 0
    timer_right = 0
    timer_forward = 0

    try:
        while True:
            light1.turn_on()
            light2.turn_on()
            time.sleep(0.2)
            if lineFollow.poll() is True:
                print("Black line")
                carClass.onBlack(75)
            else:
                print("not black line " + str(lineFollow.poll()))
                carClass.onWhite(75)

                '''
                # if voor links kijken met counter
                if timer_right < 20:
                    print("kijk naar rechts " + str(lineFollow.poll()))
                    motor1.backward(12 + timer_right)
                    motor2.forward(12 + timer_right)
                    time.sleep(0.2)
                    timer_right = timer_right + 2.5

                # if voor rechts kijken met counter
                if timer_left < 20:
                    print("kijk naar links " + str(lineFollow.poll()))
                    motor1.forward(12 + timer_left)
                    motor2.backward(12 + timer_left)
                    time.sleep(0.2)
                    timer_left = timer_left + 5

                # als bijde timers eind hebben berijkt
                if timer_left == 20 and timer_right == 20:
                    print("Kijk vooruit")
                    motor1.forward(12)
                    motor2.forward(12)
                    time.sleep(0.2)
                '''

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
