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
        """
        Sets up cart with a plural of sensors. Pins are pre-set to work with
         already set-up cart.
        """
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

    def turn_right(self, speed, ratio) -> None:
        """
        Makes cart turn. Speed is wheel speed, ratio is speed at which other
        wheel spins in the corner. -1 is turning in place, +1 would make the
        cart go straight.
        :param speed: speed 0-100
        :param ratio: ration -1 - 1
        """
        self.prev_turn = 'right'
        if ratio > 0:
            self.l_wheel.forward(speed * ratio)
            self.r_wheel.forward(speed)
        else:
            self.l_wheel.backward(speed * (ratio * -1))
            self.r_wheel.forward(speed)

    def turn_left(self, speed, ratio) -> None:
        """
        Makes cart turn. Speed is wheel speed, ratio is speed at which other
        wheel spins in the corner. -1 is turning in place, +1 would make the
        cart go straight.
        :param speed: speed 0-100
        :param ratio: ration -1 - 1
        """
        self.prev_turn = 'left'
        if ratio > 0:
            self.r_wheel.forward(speed * ratio)
            self.l_wheel.forward(speed)
        else:
            self.r_wheel.backward(speed * (ratio * -1))
            self.l_wheel.forward(speed)

    def turn_left_tick(self, ticks=1, speed=20, ratio=-1) -> None:
        """
        Makes the cart turn a pre-defined amount an n amount of times.
        :param ticks: Amount of ticks to turn
        :param speed: Speed at which to turn ( optional)
        :param ratio: Ration at which to turn ( optional)
        """
        self.turn_left(speed, ratio)
        time.sleep(0.1 * ticks)
        self.stop()

    def turn_right_tick(self, ticks=1, speed=20, ratio=-1) -> None:
        """
        Makes the cart turn a pre-defined amount an n amount of times.
        :param ticks: Amount of ticks to turn
        :param speed: Speed at which to turn ( optional)
        :param ratio: Ration at which to turn ( optional)
        """
        self.turn_right(speed, ratio)
        time.sleep(0.1 * ticks)
        self.stop()

    def stop(self) -> None:
        """
        stops the cart
        """
        self.l_wheel.stop()
        self.r_wheel.stop()

    def forward(self, speed) -> None:
        """
        Makes the cart go forward
        :param speed: Speed at which to go forward at
        """
        self.r_wheel.forward(speed)
        self.l_wheel.forward(speed)

    def backward(self, speed) -> None:
        """
        Makes the cart go backward
        :param speed: Speed at which to go backward at
        """
        self.r_wheel.backward(speed)
        self.l_wheel.backward(speed)

    def turn_on_lights(self) -> None:
        """
        Turns on front-lights
        """
        self.right_light.turn_on()
        self.left_light.turn_on()

    def turn_off_lights(self) -> None:
        """
        Turns off front-lights
        """
        self.right_light.turn_off()
        self.left_light.turn_off()

    def start_sirene(self) -> None:
        """
        Turns on the siren loop in new thread. Don't run twice without stopping.
        """
        self.running = True
        self.thread = Thread(target=self.siren_loop)
        self.thread.start()

    def stop_sirene(self) -> None:
        """
        Stops the siren from running. Don't call without sirens running.
        """
        self.running = False
        self.thread.do_run = False
        self.thread.join()

        self.red_sirene.turn_off()
        self.blue_sirene.turn_off()

    @property
    def siren_running(self) -> bool:
        """
        Wether the siren is currently on.
        :return: bool siren running?
        """
        return self.running

    def siren_loop(self) -> None:
        """
        Loops trough an American style siren loop.
        """
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
