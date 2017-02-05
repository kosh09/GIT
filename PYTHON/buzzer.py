import wiringpi2 as GPIO                     #Import GPIO library
import Ultrasonic_distance as ult
import time                                  #Import time library
GPIO.wiringPiSetup()

def buzzer():
    Buzz = x                                # x will be buzzer's Pin number
    GPIO.pinMode(Buzz,1)

    while True:
        dist = ult.distance_5()
        if dist <= 30:
            GPIO.digitalWrite(BUzz,0)
            time.sleep(dist/30)
            GPIO.digitalWrite(BUZZ, 1)
