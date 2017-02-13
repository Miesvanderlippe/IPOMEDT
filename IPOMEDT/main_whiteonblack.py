# classes importeren.
from classes.motor import Motor
from classes.lineFollower import LineFollower
from classes.ultraSonic import UltraSonic
from util.GPIOFuckUp import GPIOFuckUp
from RPi import GPIO
import time
from classes.light import Light

# Hieronder variabelen
def main() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    testmotor1 = Motor([9, 10])
    testmotor2 = Motor([7, 8])
    linefollower = LineFollower(25)
    ultrasonic = UltraSonic([17, 18])
    swich = False  # gaat standaart naar rechts draien
    teller = 0
    right_light = Light(21)  # Rechter led voorkant
    left_light = Light(13)  # Linker led voorkant
    siren_blue = Light(5)  # Links led achterkant
    #  Zwart is True
    #  Wit is False
    try:
        while True:
            distance = ultrasonic.poll() # Koppel een Variablen toe aan sensor die kijkt of hij tegen iets aan loopt
            lightsensor = linefollower.poll() # Koppel een Variablen toe aan sensor die kijkt of hij op zwart of wit rijd
            time.sleep(0.1) #  Wacht 0.1 seconden  Dit heb ik gedaan omdat hij anders te snel een meeting doet waardoor die soms vast liep
            if lightsensor is False and distance > 30:  # true als de onder sensor op zwarte opevlakte rijd en de boven sensor geen opstake heeft gevonden
                print("Auto rijd op zwart. afstand",distance) #  Toon op het scherm de volgende bericht Auto rijd op zwart een de afstand is : De waarden die de sensor leest.
                testmotor1.forward(100) #  Geef vollen gas naar voren met motor1
                testmotor2.forward(100) # Geef vollen gas naar voren met motor2
                siren_blue.turn_off() #  zet de achter led uit
                right_light.turn_on()  # zet de rechter led aan
                left_light.turn_on()  # zet de linker led aan

            elif lightsensor is False and distance < 30 and swich is False and teller < 5:  # hij kijkt of hij op het witte is als dat waar is rijdt hij een stuk terug.
                left_light.turn_off()  # zet de linker led uit
                right_light.turn_on()  # zet de rechter led aan
                print(" Gaat naar rechts. de afstand is ", distance,teller) #  Toon op het scherm de volgende bericht rechts "Gaat naar rechts. De afstand: De waarden die de sensor leest "
                testmotor1.stop() #  Stop de motoren
                testmotor2.stop() #  Stop de motoren
                time.sleep(0.1) #  Wacht 0.1 seconden
                testmotor1.backward(80)  # linker wiel
                testmotor2.forward(100)  # rechter wiel
                time.sleep(1.2) #  Wacht 3.5 seconden
                swich = True # zet de schakelaar op True
                teller += 1 #  Verhoog de teller met 1

            elif lightsensor is False and distance < 30 and swich is True and teller < 5: #  Als hij op Zwart rijd
                right_light.turn_off()  # zet de rechter led uit
                left_light.turn_on()  # zet de linker led aan
                print("Gaat naar links. de afstand is ", distance, teller) #  Toon op het scherm de volgende bericht "Gaat naar links. de afstand is. De afstand: De waarden die de sensor leest.
                testmotor1.stop() #  Stop de motoren
                testmotor2.stop() #  Stop de motoren
                testmotor2.backward(80) #  Ga naar achteren met motor2
                testmotor1.forward(100) #  Ga naar voor met motor1
                time.sleep(1.2) #  Wacht 3.5 seconden
                swich = False #  zet de schakelaar op False
                teller += 1 #  Verhoog de teller met 1

            elif teller == 5: #  Als de teller op 5 zit voer dit uit
                right_light.turn_off()  # zet de rechter led uit
                left_light.turn_off()  # zet de linker led uit
                siren_blue.turn_on()  # zet de achter led aan
                print("achteruit Let: op !")
                testmotor1.stop() #  Stop de motoren
                testmotor2.stop() # Stop de motoren
                testmotor1.backward(100) #  Ga naar achteren
                testmotor2.backward(100) # Ga naar achteren
                time.sleep(1.5) #  Wacht anderhalf seconden
                teller = 0 #  Zet de teller op nul

            elif lightsensor is True:
                siren_blue.turn_on()  # zet de achter led aan
                right_light.turn_on()  # zet de rechter led aan
                left_light.turn_on()  # zet de linker led aan
                print("Auto rijd op wit", distance)
                print(distance)
                testmotor1.stop()
                testmotor2.stop()
                GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    GPIOFuckUp()
    main()