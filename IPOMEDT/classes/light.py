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

    left_light = Light(21)
    right_light = Light(20)

    left_light.turn_on()
    time.sleep(1)

    right_light.turn_on()
    time.sleep(1)

    right_light.turn_off()
    left_light.turn_off()

if __name__ == '__main__':
    main()
