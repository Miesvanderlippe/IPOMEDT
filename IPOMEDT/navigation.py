from classes import motor
from classes import lineFollower

def main() -> None:

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    motor1 = Motor([10, 9])
    moter2 = Moter([8, 7])

    lineFollow = LineFollower()

    while True:
        sleep(0.1)
        if lineFollow == True :
            print("Blue line")
            motor1.forward()
            motor2.forward()
            sleep(0.5)
        else:
            print("not blue line")
            motor1.stop()
            motor2.stop()

if __name__ == __main__ :
    main()
