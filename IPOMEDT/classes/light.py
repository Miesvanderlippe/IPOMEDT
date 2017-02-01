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

    right_light = Light(21)
    left_light = Light(20)
    siren_blue = Light(16)
    siren_red = Light(26)

    left_light.turn_on()
    time.sleep(2)

    right_light.turn_on()
    time.sleep(2)

    siren_blue.turn_on()
    time.sleep(2)

    siren_red.turn_on()
    time.sleep(2)

    for i in range(0, 100):
        right_light.dim(i)
        left_light.dim(i)
        time.sleep(0.1)

    right_light.turn_off()
    left_light.turn_off()
    siren_red.turn_off()
    siren_blue.turn_off()



if __name__ == '__main__':
    main()

