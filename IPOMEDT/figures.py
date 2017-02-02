from classes.cart import Cart
from random import randint
from RPi import GPIO
import time


def main():

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    car = Cart()
    cnt = 0

    dist = 0
    last_dist = 0

    while True:
        dist = round(car.ultrasonic.poll())
        speed = randint(10, 70)
        turn_factor = randint(1, 10) / 10

        car.forward(40)
        time.sleep(1.5)

        if dist == last_dist:
            car.backward(50)
            time.sleep(0.5)
            car.turn_right_tick(8)

        if cnt % 2 == 0:
            car.turn_left(speed, turn_factor)
        else:
            car.turn_right(speed, turn_factor)

        time.sleep(cnt % 3)
        cnt += 1
        last_dist = dist

if __name__ == "__main__":
    main()
