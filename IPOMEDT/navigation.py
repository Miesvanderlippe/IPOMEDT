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

    try:
        while True:
            light.turn_on()
            sleep(0.1)
            if lineFollow == True :
                print("Blue line")
                motor1.forward()
                motor2.forward()
                sleep(0.2)
            else:
                print("not blue line")
                motor1.stop()
                motor2.stop()
                sleep(0.2)
                #kijk naar rechts
                #kijk naar links

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == __main__ :
    main()