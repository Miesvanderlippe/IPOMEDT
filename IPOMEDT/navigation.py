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

    light = Light(21)

    lineFollow = LineFollower(25)
    carClass = CarClass()

    direction_time = 30

    try:
        while True:
            light.turn_on()
            time.sleep(0.1)
            if lineFollow.poll() is True:
                print("Black line")
                motor1.forward(12)
                motor2.forward(12)
                time.sleep(0.2)
            else:
                print("not black line " + str(lineFollow.poll()))
                motor1.stop()
                motor2.stop()
                time.sleep(0.5)

                while lineFollow.poll() is False:
                    time.sleep(0.5)
                    if direction_time <= 30:
                        # kijk rechts
                        print("kijk naar rechts " + str(lineFollow.poll()))
                        # carClass.turnRight(12, 5)
                        motor1.forward(12)
                        motor2.backward(12)
                        direction_time = direction_time - 1

                    # timer terug naar 30
                    direction_time = 30

                    if direction_time <= 30:
                        # kijk links
                        print("kijk naar links " + str(lineFollow.poll()))
                        motor1.backward(12)
                        motor2.forward(12)
                        # carClass.turnLeft(12, 5)
                        direction_time = direction_time - 1

                    # timer terug naar 30
                    direction_time = 30

                    if direction_time <= 30:
                        # kijk vooruit
                        print("kijk vooruit " + str(lineFollow.poll()))
                        motor1.forward(12)
                        motor2.forward(12)
                        direction_time = direction_time - 1

                    # timer terug naar 30
                    direction_time = 30
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
