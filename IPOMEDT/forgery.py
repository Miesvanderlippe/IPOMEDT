from RPi import GPIO
import time


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    pins = [10, 8]

    GPIO.setup(pins[0], GPIO.OUT)
    GPIO.setup(pins[1], GPIO.OUT)

    pin1 = GPIO.PWM(pins[0], 10)
    pin2 = GPIO.PWM(pins[1], 10)

    pin1.start(50)
    pin2.start(50)

    time.sleep(0.5)

    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)

    GPIO.output(10, 1)
    GPIO.output(8, 1)

    time.sleep(5)

if __name__ == "__main__":
    main()
