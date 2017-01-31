import time
from classes import light
from classes import motor
from classes import lineFollower

def main() -> None:

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    motor1 = Motor([10, 9])
    moter2 = Moter([8, 7])

    light = Light()

    lineFollow = LineFollower()

    direction_time =  30

    try:
        while True:
            light.turn_on()
            sleep(0.1)
            if lineFollow == True :
                print("Blue line")
                motor1.forward(30)
                motor2.forward(30)
                sleep(0.2)
            else:
                print("not blue line")
                motor1.stop()
                motor2.stop()
                sleep(0.2)

                while lineFollow == False :
                    if direction_time <= 30 :
                        #kijk rechts
                        print("kijk naar rechts")
                        direction_time =- 1

                    #timer terug naar 30
                    direction_time = 30

                    if direction_time <= 30 :
                        #kijk links
                        print("kijk naar links")
                        direction_time =- 1

                    #timer terug naar 30
                    direction_time = 30

                    if direction_time <= 30 :
                        #kijk vooruit
                        print("kijk vooruit")
                        direction_time =- 1

                    #timer terug naar 30
                    direction_time = 30

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == __main__ :
    main()