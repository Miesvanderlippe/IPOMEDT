from classes.ultraSonic import UltraSonic
from classes.cart import Cart
import RPi.GPIO as GPIO
import time


def main() -> None:

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    cart = Cart()
    ultrasonic = UltraSonic([17, 18])
    direction = False
    loopcount = 0

    for i in range(1, 16):
        distance = ultrasonic.poll()
        print(distance)

        if i % 2 == 1:
            cart.turn_right(17, -1)
        else:
            cart.turn_left(17, -1)

        time.sleep(0.07 * i)
        cart.stop()

    while True and False:

        distance = ultrasonic.poll()

        print("dis: {0}".format(distance))

        if distance < 10 and distance > 1:
            cart.stop()

        elif distance < 30 and distance > 1:
            cart.forward(16)
            time.sleep(0.2)
            cart.stop()

        elif distance > 30 or distance < 1:

            if (loopcount % 10) == 0:
                direction = not direction

            loopcount += 1

            print("{0} : {1}".format(direction, loopcount))

            if direction:
                cart.turn_right(17, -1)
            else:
                cart.turn_left(17, -1)

            time.sleep(0.2)
            cart.stop()


if __name__ == "__main__":
    main()
