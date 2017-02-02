import time
from classes.motor import Motor


class CarClass:

    def __init__(self):
        self.motor1 = Motor([10, 9])
        self.motor2 = Motor([8, 7])

    '''
    Als op zwart is
    stuur motor1 forward en motor2 backward met lagere speed
    en motor1 stukje naar voor
    '''
    def onBlack(self, speed):
        self.motor1.forward(speed)
        self.motor2.backward(speed - (speed / 3))
        self.motor1.forward(10)

    '''
    Als op wit is
    stuur motor2 forward en motor1 backward met lagere speed
    en motor2 stukje naar voor
    '''

    def onWhite(self, speed):
        self.motor2.forward(speed)
        self.motor1.backward(speed - (speed / 3))
        self.motor2.forward(10)
