import wiringpi2 as GPIO                     #Import wiringpi2 library
import time                                  #Import time library
GPIO.wiringPiSetup()                         #Set wiringpi2 pin numbering 
def Blink():
    LED = 2                                  #Associate pin ? to LED
    
    GPIO.pinMode(LED,1)                      #Set pin as GPIO out
    
    while True:
      GPIO.digitalWrite(TRIG, 1)             #Set LED as HIGH
      time.sleep(1)                          #Wait for 1 second
      GPIO.digitalWrite(LED, 0)              #Set LED as LOW
      time.sleep(1)                          #Wait for 1 second
