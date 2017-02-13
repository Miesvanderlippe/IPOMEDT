'''IMPORTEREN VAN ALLE LIBRARY'S'''
import RPi.GPIO as GPIO
import time
import random
#---------------------------------------------------------

'''PINMODES AANGEVEN'''
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#---------------------------------------------------------

'''OP WELKE PINS ZITTEN DE MOTOREN'''
pinLinksVooruit = 10
pinLinksAchteruit = 9
pinRechtsVooruit = 8
pinRechtsAchteruit = 7
#---------------------------------------------------------

'''OP WELKE PINS ZITTEN DE 'OGEN' '''
pinStuurSignaal = 17
pinOntvangSignaal = 18
#---------------------------------------------------------

'''OP WELKE PINS ZITTEN DE LICHTSENSOREN'''
pinLichtSensor = 25
#---------------------------------------------------------

'''OP WELKE PINS ZITTEN DE LEDJES'''
pinLED1 = 22
pinLED2 = 23
#----------------------------------------------------------

'''FREQUENTIE VAN DE WIELEN, HOEVAAK AAN/UIT PER SECONDE'''
frequentie = 10
#---------------------------------------------------------

'''PROCENTEN DAT DE WIELEN AAN MOETEN STAAN'''
rondjesLinks = 50
rondjesRechts = 30
#---------------------------------------------------------

'''VARIABELE VOOR HET STOPPEN VAN DE AUTO'''
stop = 0
#---------------------------------------------------------

'''de variablen omtrent motor-snelheid'''
snelheidWielLinks = 100
snelheidWielRechts = 83
snelheidMaal = .37
#---------------------------------------------------------

'''ZIJN DE PINNEN IN/OUT-PUT'''
GPIO.setup(pinLinksVooruit, GPIO.OUT)
GPIO.setup(pinLinksAchteruit, GPIO.OUT)
GPIO.setup(pinRechtsVooruit, GPIO.OUT)
GPIO.setup(pinRechtsAchteruit, GPIO.OUT)

GPIO.setup(pinStuurSignaal, GPIO.OUT)
GPIO.setup(pinOntvangSignaal, GPIO.IN)

GPIO.setup(pinLichtSensor, GPIO.IN)

GPIO.setup(pinLED1, GPIO.OUT)
GPIO.setup(pinLED2, GPIO.OUT)
#---------------------------------------------------------

'''VARIABELEN VOOR AFSTANDSMETING'''
hoeDichtBij = 35.0
draaiTijd = 0.75
#---------------------------------------------------------

'''ZET PWM OP 'FREQUENTIE' '''
pwmMotorLinksVooruit = GPIO.PWM(pinLinksVooruit, frequentie)
pwmMotorLinksAchteruit = GPIO.PWM(pinLinksAchteruit, frequentie)
pwmMotorRechtsVooruit = GPIO.PWM(pinRechtsVooruit, frequentie)
pwmMotorRechtsAchteruit = GPIO.PWM(pinRechtsAchteruit, frequentie)
#---------------------------------------------------------

'''ZET ALLES UIT'''
pwmMotorLinksVooruit.start(stop)
pwmMotorLinksAchteruit.start(stop)
pwmMotorRechtsVooruit.start(stop)
pwmMotorRechtsAchteruit.start(stop)
#---------------------------------------------------------

'''FUNCTIE VOOR ALLE MOTORS UIT'''
def motorsUit():
    pwmMotorLinksVooruit.ChangeDutyCycle(stop)
    pwmMotorLinksAchteruit.ChangeDutyCycle(stop)
    pwmMotorRechtsVooruit.ChangeDutyCycle(stop)
    pwmMotorRechtsAchteruit.ChangeDutyCycle(stop)
#---------------------------------------------------------

'''FUNCTIE VOOR VOORUIT'''
def rijVooruit():
    pwmMotorLinksVooruit.ChangeDutyCycle(snelheidWielLinks * snelheidMaal)
    pwmMotorLinksAchteruit.ChangeDutyCycle(0)
    pwmMotorRechtsVooruit.ChangeDutyCycle(snelheidWielRechts * snelheidMaal)
	pwmMotorLinksAchteruit.ChangeDutyCycle(0)
#---------------------------------------------------------

'''FUNCTIE VOOR ACHTERUIT'''
def rijAchteruit():
    pwmMotorLinksVooruit.ChangeDutyCycle(0)
	pwmMotorLinksAchteruit.ChangeDutyCycle(snelheidWielLinks * snelheidMaal)
	pwmMotorRechtsVooruit.ChangeDutyCycle(0)
	pwmMotorRechtsAchteruit.ChangeDutyCycle(snelheidWielRechts * snelheidMaal)
#---------------------------------------------------------

'''FUNCTIE VOOR LINKS'''
def Links():
    pwmMotorLinksVooruit.ChangeDutyCycle(snelheidWielLinks * snelheidMaal)
	pwmMotorLinksAchteruit.ChangeDutyCycle(0)
	pwmMotorRechtsVooruit.ChangeDutyCycle(0)
	pwmMotorRechtsAchteruit.ChangeDutyCycle(snelheidWielRechts * snelheidMaal)
#---------------------------------------------------------

'''FUNCTIE VOOR RECHTS'''
def Rechts():
    pwmMotorLinksVooruit.ChangeDutyCycle(0)
	pwmMotorLinksAchteruit.ChangeDutyCycle(snelheidWielLinks * snelheidMaal)
	pwmMotorRechtsVooruit.ChangeDutyCycle(snelheidWielRechts * snelheidMaal)
	pwmMotorRechtsAchteruit.ChangeDutyCycle(0)
#---------------------------------------------------------

'''FUNCITE VOOR AFSTAND METEN'''
def meetAfstand():
    GPIO.output(pinStuurSignaal, True)
    time.sleep(0.00001)
    GPIO.output(pinStuurSignaal, False)
    StartTime = time.time()
    StopTime = StartTime
    while GPIO.input(pinOntvangSignaal) == 0:
        StartTime = time.time()
        StopTime = StartTime
    while GPIO.input(pinOntvangSignaal) == 1:
        StopTime = time.time()
    return ((StopTime-StartTime)*34326)/2
#---------------------------------------------------------

'''DETECTEREN VAN OBSTAKEL'''
def isObstakel(lokaleHoeDichtBij):
    return meetAfstand() < lokaleHoeDichtBij
#---------------------------------------------------------

'''HOOFDCODE'''
try:
	while True:
		if GPIO.input(pinLichtSensor) == 0:
			rijVooruit()
            GPIO.output(pinLED1, 0)
            GPIO.output(pinLED2, 1)
		else:
			Links()
            GPIO.output(pinLED1, 1)
            GPIO.output(pinLED2, 0)

#CTRL + C stoppen de motoren
except KeyboardInterrupt:
	running = False
	GPIO.cleanup()