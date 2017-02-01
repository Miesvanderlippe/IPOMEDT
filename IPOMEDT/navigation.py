import time
import RPi.GPIO as GPIO
from classes.light import Light
from classes.motor import Motor
from classes.carClass import CarClass
from classes.lineFollower import LineFollower


def main() -> None:

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)

    motor1 = Motor([10, 9])
    motor2 = Motor([8, 7])

    light = Light(21)

    lineFollow = LineFollower(25)
    carClass = CarClass()

    direction_time = 30

    try:
        while True:
            light.turn_on()
            time.sleep(0.1)
            if lineFollow.poll() is True:
                print("Blue line")
                motor1.forward(5)
                motor2.forward(5)
                time.sleep(0.2)
            else:
                print("not blue line " + str(lineFollow.poll()))
                motor1.stop()
                motor2.stop()
                time.sleep(0.5)

                while lineFollow.poll() is False:
                    time.sleep(0.5)
                    if direction_time <= 30:
                        # kijk rechts
                        print("kijk naar rechts " + str(lineFollow.poll()))
                        carClass.turnRight(15, 5)
                        direction_time = direction_time - 1

                    # timer terug naar 30
                    direction_time = 30

                    if direction_time <= 30:
                        # kijk links
                        print("kijk naar links " + str(lineFollow.poll()))
                        carClass.turnLeft(15, 5)
                        direction_time = direction_time - 1

                    # timer terug naar 30
                    direction_time = 30

                    if direction_time <= 30:
                        # kijk vooruit
                        print("kijk vooruit " + str(lineFollow.poll()))
                        motor1.forward(15)
                        motor2.forward(15)
                        direction_time = direction_time - 1

                    # timer terug naar 30
                    direction_time = 30
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
