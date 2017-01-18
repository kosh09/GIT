import wiringpi2 as GPIO                     #Import GPIO library
import time                                  #Import time library
GPIO.wiringPiSetup()                         #Set GPIO pin numbering

def distance_2():   # 전방입니다.
    TRIG = 2                                  #Associate pin 23 to TRIG
    ECHO = 3                                  #Associate pin 24 to ECHO

    GPIO.pinMode(TRIG,1)                      #Set pin as GPIO out
    GPIO.pinMode(ECHO,0)                      #Set pin as GPIO in

    while True:
      GPIO.digitalWrite(TRIG, 0)                 #Set TRIG as LOW
      time.sleep(0.2)

      GPIO.digitalWrite(TRIG, 1)                  #Set TRIG as HIGH
      time.sleep(0.00001)                      #Delay of 0.00001 seconds
      GPIO.digitalWrite(TRIG, 0)                 #Set TRIG as LOW

      while GPIO.digitalRead(ECHO)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

      while GPIO.digitalRead(ECHO)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

      pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

      distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
      distance = round(distance, 2)            #Round to two decimal points
      distance = distance - 1

      if distance > 2 and distance < 400:      #Check whether the distance is within range
        #print ("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
        return distance
        
def distance_5():
    TRIG = 4                                  #Associate pin 23 to TRIG
    ECHO = 5                                  #Associate pin 24 to ECHO

    GPIO.pinMode(TRIG,1)                      #Set pin as GPIO out
    GPIO.pinMode(ECHO,0)                      #Set pin as GPIO in

    while True:
      GPIO.digitalWrite(TRIG, 0)                 #Set TRIG as LOW
      time.sleep(0.2)

      GPIO.digitalWrite(TRIG, 1)                  #Set TRIG as HIGH
      time.sleep(0.00001)                      #Delay of 0.00001 seconds
      GPIO.digitalWrite(TRIG, 0)                 #Set TRIG as LOW

      while GPIO.digitalRead(ECHO)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

      while GPIO.digitalRead(ECHO)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

      pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

      distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
      distance = round(distance, 2)            #Round to two decimal points
      distance = distance - 1

      if distance > 2 and distance < 400:      #Check whether the distance is within range
        #print ("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
        return distance


def distance_8():                           # LEFT
    TRIG = 21                                  #Associate pin 23 to TRIG
    ECHO = 22                                  #Associate pin 24 to ECHO

    GPIO.pinMode(TRIG,1)                      #Set pin as GPIO out
    GPIO.pinMode(ECHO,0)                      #Set pin as GPIO in

    while True:
      GPIO.digitalWrite(TRIG, 0)                 #Set TRIG as LOW
      time.sleep(0.2)

      GPIO.digitalWrite(TRIG, 1)                  #Set TRIG as HIGH
      time.sleep(0.00001)                      #Delay of 0.00001 seconds
      GPIO.digitalWrite(TRIG, 0)                 #Set TRIG as LOW

      while GPIO.digitalRead(ECHO)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

      while GPIO.digitalRead(ECHO)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

      pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

      distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
      distance = round(distance, 2)            #Round to two decimal points
      distance = distance - 1

      if distance > 2 and distance < 400:      #Check whether the distance is within range
        #print ("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
        return distance

def distance_7():                               # RIGHT
    TRIG = 6                                  #Associate pin 23 to TRIG
    ECHO = 11                                  #Associate pin 24 to ECHO

    GPIO.pinMode(TRIG,1)                      #Set pin as GPIO out
    GPIO.pinMode(ECHO,0)                      #Set pin as GPIO in

    while True:
      GPIO.digitalWrite(TRIG, 0)                 #Set TRIG as LOW
      time.sleep(0.2)

      GPIO.digitalWrite(TRIG, 1)                  #Set TRIG as HIGH
      time.sleep(0.00001)                      #Delay of 0.00001 seconds
      GPIO.digitalWrite(TRIG, 0)                 #Set TRIG as LOW

      while GPIO.digitalRead(ECHO)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

      while GPIO.digitalRead(ECHO)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

      pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

      distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
      distance = round(distance, 2)            #Round to two decimal points
      distance = distance - 1

      if distance > 2 and distance < 400:      #Check whether the distance is within range
        #print ("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
        return distance
