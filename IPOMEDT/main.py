from classes.ultraSonic import UltraSonic
from classes.cart import Cart
import RPi.GPIO as GPIO
import time


def main() -> None:

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    cart = Cart()
    direction = False

    while True:

        distance = cart.ultrasonic.poll()

        print("dis: {0}".format(distance))

        if distance < 10 and distance > 1:
            cart.stop()

        elif distance < 50 and distance > 1:
            cart.forward(distance * 2)
            time.sleep(0.2)
            cart.stop()

        elif distance > 50 or distance < 1:

            print("{0}".format(cart.prev_turn))

            for i in range(0, 10):

                direction = cart.prev_turn != 'right'

                if direction:
                    cart.turn_right_tick(i)
                else:
                    cart.turn_left_tick(i)

                print("Turning {0} {1}".format(cart.prev_turn, i))

                distance = cart.ultrasonic.poll()

                if distance > 1 and distance < 30:
                    break

            for i in range(0, 10):
                cart.turn_right_tick(1)
                distance = cart.ultrasonic.poll()

                if distance > 1 and distance < 30:
                    break


if __name__ == "__main__":
    main()
