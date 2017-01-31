from classes.motor import Motor
from classes.lineFollower import LineFollower
from classes.ultraSonic import UltraSonic
from classes.light import Light


def main() -> None:
    testmotor1 = Motor([10, 9])
    testmotor2 = Motor([8, 7])
    linefollower = LineFollower(25)
    ultrasonic = UltraSonic([17, 18])

    testmotor1 = Motor([10, 9])
    testmotor2 = Motor([8, 7])

    sensor = UltraSonic([17, 18])
    distance = sensor.poll

    if distance > 1:
        testmotor1.forward()
        testmotor2.forward()
    elif distance < 1:
        testmotor1.forward()
        time.sleep(0.5)
        testmotor2.backward()
        time.sleep(0.5)


if __name__ == "__main__":
    main()
