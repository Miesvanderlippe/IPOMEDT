from IPOMEDT.classes.motor import Motor
from IPOMEDT.classes.lineFollower import LineFollower
from IPOMEDT.classes.ultraSonic import UltraSonic


def main() -> None:
    testmotor1 = Motor([10, 9])
    testmotor2 = Motor([8, 7])
    linefollower = LineFollower(25)
    ultrasonic = UltraSonic([17, 18])

    raise NotImplementedError()

if __name__ == "__main__":
    main()
