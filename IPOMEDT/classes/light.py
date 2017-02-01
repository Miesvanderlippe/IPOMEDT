import RPi.GPIO as GPIO
import time


class Light:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    left_light = Light(26)
    right_light = Light(21)
    red_sirene = Light(20)
    blue_sirene = Light(16)

    left_light.turn_off()
    right_light.turn_off()
    red_sirene.turn_off()
    blue_sirene.turn_off()

    time.sleep(2)

    left_light.turn_on()
    time.sleep(0.5)
    right_light.turn_on()
    time.sleep(0.5)
    red_sirene.turn_on()
    time.sleep(0.5)
    blue_sirene.turn_on()
    time.sleep(0.5)

    time.sleep(10)

    left_light.turn_off()
    right_light.turn_off()
    red_sirene.turn_off()
    blue_sirene.turn_off()

if __name__ == '__main__':
    main()
