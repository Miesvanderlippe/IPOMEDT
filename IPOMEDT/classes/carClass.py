from classes.motor import Motor


class CarClass:

    def __init__(self):
        self.motor1 = Motor([10, 9])
        self.motor2 = Motor([8, 7])

    def turnLeft(self, speed, ratio):
        self.motor1.forward(speed + ratio)
        self.motor2.backward(speed + ratio)

    def turnRight(self, speed, ratio):
        self.motor1.backward(speed + ratio)
        self.motor2.forward(speed + ratio)
