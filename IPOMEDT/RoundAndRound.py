# CamJam EduKit 3 - Robotics
# Worksheet 9 – Obstacle Avoidance
import RPi.GPIO as GPIO  # Import the GPIO Library
import time
# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7
pinTrigger = 17
pinEcho = 18
# How many times to turn the pin on and off each second Frequency = 20
Frequency = 20
# How long the pin stays on each cycle, as a percent DutyCycleA = 30
DutyCycleB = 10
DutyCycleA = 10
# Setting the duty cycle to 0 means the motors will not turn
Stop = 0

GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)
# Set pins as output and input
GPIO.setup(pinTrigger, GPIO.OUT)  # Trigger
GPIO.setup(pinEcho, GPIO.IN)      # Echo
# Distance Variables
HowNear = 15.0
ReverseTime = 0.5
TurnTime = 0.75
# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency) pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency) pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency) pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)
# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)


# Turn all motors off
def StopMotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)


def Forwards(speed):
    pwmMotorAForwards.ChangeDutyCycle(speed)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(speed)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)


# Turn both motors backwards
def Backwards(speed):
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(speed)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(speed)


# Turn left
def Left(speed):
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(speed)
    pwmMotorBForwards.ChangeDutyCycle(speed)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)


# Take a distance measurement
def Measure():
    GPIO.output(pinTrigger, True)
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)
    StartTime = time.time()
    StopTime = StartTime
    while GPIO.input(pinEcho) == 0:
        StartTime = time.time()
    StopTime = StartTime
    while GPIO.input(pinEcho) == 1:
        StopTime = time.time()
    # If the sensor is too close to an object, the Pi cannot # see the echo quickly enough, so it has to detect that # problem and say what has happened
        if StopTime - StartTime >= 0.04:
                print("Hold on there!  You're too close for me to see.")
                StopTime = StartTime
        break

    ElapsedTime = StopTime - StartTime
    Distance = (ElapsedTime * 34326) / 2

    print("IsNearObstacle: " + str(Distance))
    if Distance < HowNear:
        return True
    return False


# Move back a little, then turn right
def AvoidObstacle():
    # Back off a little
    print("Going Left")
    time.sleep(ReverseTime)
    Forwards()
# Turn left
    print("Right")
    Left()
    time.sleep(TurnTime)
    StopMotors()
# Your code to control the robot goes below this line try:
    # Set trigger to False (Low)
    GPIO.output(pinTrigger, False)
    # Allow module to settle
    time.sleep(0.1)
# repeat the next indented block forever
try:
    while True:
        Forwards(10)
        time.sleep(0.1)
        if Measure():
            Forwards(10)
            AvoidObstacle()
# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()
