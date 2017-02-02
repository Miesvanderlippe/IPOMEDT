import time
from classes.motor import Motor


class CarClass:

    def __init__(self):
        self.motor1 = Motor([10, 9])
        self.motor2 = Motor([8, 7])

    def onBlack(self, speed):
        self.motor1.forward(speed)
        self.motor2.backward(speed - (speed / 3))
        self.motor1.forward(10)

    def onWhite(self, speed):
        self.motor1.backward(speed - (speed / 3))
        self.motor2.forward(speed)
        self.motor1.backward(10)
