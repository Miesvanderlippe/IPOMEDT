import RPi.GPIO as GPIO
import time
from threading import Thread

if __name__ == "__main__":
    from motor import Motor
    from ultraSonic import UltraSonic
    from light import Light
else:
    from classes.motor import Motor
    from classes.ultraSonic import UltraSonic
    from classes.light import Light


class Cart:

    def __init__(self):
        self.l_wheel = Motor([9, 10])
        self.r_wheel = Motor([7, 8])
        self.left_light = Light(20)
        self.right_light = Light(21)
        self.red_sirene = Light(26)
        self.blue_sirene = Light(16)

        self.ultrasonic = UltraSonic([17, 18])
        self.prev_turn = 'left'
        self.running = False
        self.thread = None

    def turn_right(self, speed, ratio):
        self.prev_turn = 'right'
        if ratio > 0:
            self.l_wheel.forward(speed * ratio)
            self.r_wheel.forward(speed)
        else:
            self.l_wheel.backward(speed * (ratio * -1))
            self.r_wheel.forward(speed)

    def turn_left(self, speed, ratio):
        self.prev_turn = 'left'
        if ratio > 0:
            self.r_wheel.forward(speed * ratio)
            self.l_wheel.forward(speed)
        else:
            self.r_wheel.backward(speed * (ratio * -1))
            self.l_wheel.forward(speed)

    def turn_left_tick(self, ticks=1, speed=20, ratio=-1):
        self.turn_left(speed, ratio)
        time.sleep(0.1 * ticks)
        self.stop()

    def turn_right_tick(self, ticks=1, speed=20, ratio=-1):
        self.turn_right(speed, ratio)
        time.sleep(0.1 * ticks)
        self.stop()

    def stop(self):
        self.l_wheel.stop()
        self.r_wheel.stop()

    def forward(self, speed):
        self.r_wheel.forward(speed)
        self.l_wheel.forward(speed)

    def backward(self, speed):
        self.r_wheel.backward(speed)
        self.l_wheel.backward(speed)

    def turn_on_lights(self):
        self.right_light.turn_on()
        self.left_light.turn_on()

    def turn_off_lights(self):
        self.right_light.turn_off()
        self.left_light.turn_off()

    def start_sirene(self):
        self.running = True
        self.thread = Thread(target=self.siren_loop)
        self.thread.start()

    def stop_sirene(self):
        self.running = False
        self.thread.do_run = False
        self.thread.join()

        self.red_sirene.turn_off()
        self.blue_sirene.turn_off()

    @property
    def siren_running(self):
        return self.running

    def siren_loop(self):
        while self.running:
            self.red_sirene.turn_on()
            self.blue_sirene.turn_on()
            time.sleep(0.05)

            self.red_sirene.turn_off()
            self.blue_sirene.turn_off()
            time.sleep(0.05)

            self.blue_sirene.turn_on()
            time.sleep(0.05)

            self.blue_sirene.turn_off()
            time.sleep(0.05)

            self.red_sirene.turn_on()
            time.sleep(0.05)

            self.red_sirene.turn_off()
            time.sleep(0.05)


def main() -> None:

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    cart = Cart()

    cart.start_sirene()

    time.sleep(2)
    cart.stop_sirene()

    time.sleep(2)
    cart.start_sirene()
    cart.turn_on_lights()

    time.sleep(2)
    cart.turn_off_lights()
    cart.stop_sirene()

if __name__ == "__main__":
    main()
