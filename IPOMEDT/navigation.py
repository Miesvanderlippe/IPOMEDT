import time
from classes.light import Light
from classes.motor import Motor
from classes.carClass import CarClass
import RPi.GPIO as GPIO
from classes.lineFollower import LineFollower

def main() -> None:

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    motor1 = Motor([10, 9])
    motor2 = Motor([8, 7])

    light = Light(21)

    lineFollow = LineFollower(25)
    carClass = CarClass()

    direction_time =  30

    try:
        while True:
            light.turn_on()
            time.sleep(0.1)
            if lineFollow.poll() == False:
                print("Blue line")
                motor1.backward(5)
                motor2.backward(5)
                time.sleep(0.2)
            else:
                print("not blue line " + str(lineFollow.poll()))
                motor1.stop()
                motor2.stop()
                time.sleep(0.5)

                while lineFollow.poll() == True:
                    time.sleep(0.5)
                    if direction_time <= 30:
                        #kijk rechts
                        print("kijk naar rechts " + str(lineFollow.poll()))
                        #motor1.forward(15)
                        #motor2.stop()
                        direction_time =- 1

                    #timer terug naar 30
                    direction_time = 30

                    if direction_time <= 30:
                        #kijk links
                        print("kijk naar links " + str(lineFollow.poll()))
                        carClass.turnLeft(15, 5)
                        direction_time =- 1

                    #timer terug naar 30
                    direction_time = 30

                    if direction_time <= 30:
                        #kijk vooruit
                        print("kijk vooruit " + str(lineFollow.poll()))
                        #motor1.backward(15)
                        #motor2.backward(15)
                        direction_time =- 1

                    #timer terug naar 30
                    direction_time = 30
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
