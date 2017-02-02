import time
from classes.light import Light
from classes.motor import Motor


class CarClass:

    def __init__(self):
        self.motor1 = Motor([10, 9])
        self.motor2 = Motor([8, 7])
        self.roodlicht = Light(20)
        self.blauwlicht = Light(16)

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

    '''
    Doet lichten aan en uit
    '''

    def light(self):
        self.roodlicht.turn_on()
        time.sleep(2)
        self.blauwlicht.turn_on()
        self.roodlicht.turn_off()
        time.sleep(2)
        self.blauwlicht.turn_off()
