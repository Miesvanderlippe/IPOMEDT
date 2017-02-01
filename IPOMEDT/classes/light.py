import RPi.GPIO as GPIO
import time


class Light:

    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = GPIO.PWM(pin, 1000)
        self.pin.start(0)

    def turn_on(self):
        self.pin.ChangeDutyCycle(100)

    def turn_off(self):
        self.pin.ChangeDutyCycle(0)

    def dim(self, percentage):
        self.pin.ChangeDutyCycle(percentage)


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

