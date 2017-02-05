
# Import other python files
import BT_Serial as bt
import Parking_algorithm as park
import Laser_distance as laser
import Ultrasonic_distance as ult
import play
import LED_BLINK as LED
from Buzzer as Bu

# Import internal modules
from multiprocessing import Process
import time

def driving(a):                     # Definite Driving sequences
    bt.DRIVING()
    print('',a)
def SIG_Mode(a):
    data = bt.Mode_SIGNAL()
    return data
def SIG_LED(a):
    data = bt.LED_SIGNAL()
def parking(a):                     # Definitie Parking sequences
    park.Parking()
def alarm_parking(a):               # Alarm when parking is available
    park.Alarm()
def LED(a):                         # Blink Back LED
    LED.Blink()
def Buzzer():
    Bu.Buzzer()

if __name__ == '__main__':
    drive = process(target = driving, args =('',))          # DRIVING Sequence
    park = process(target = parking, args =('',))           # PARKING Sequence
    Led = process(target = LED, args =('',))                # BLINKING LED
    Alarm = process(target = alarm_parking, args =('',))    # ALARM When Parking is Available
    S_Mode = process(target = SIG_Mode, args =('',))        # RECEIVE SIGNAL for Mode Selection
    S_LED = process(target = SIG_LED, args =('',))          # RECEIVE SIGNAL for LED
    Buzzer = process(target = Buzzer, args =('',))          # RING the Buzzer

    play.wel()
    time.sleep(1)

    Alarm.start()
    time.sleep(1)

    play.alarm()
    time.sleep(1)

    play.s_p()
    time.sleep(2)
    drive.start()

    while True:
        SI_Mode = bt.Mode_SIGNAL()
        SI_LED = bt.LED_SIGNAL()

        LED.Blink(SI_LED)

        if SI_Mode == None:
            continue

        if SI_Mode != 80:
            drive.terminate()
            drive.join()
            play.f_d()
            time.sleep(1)
            LED.start()
            time.sleep(0.5)
            play.s_p()
            time.sleep(1)
            park.start()    # 주차 알고리즘에 주차가 끝났을때만 음악 재생되게 하고 시작재생은 여기서 하는걸로

        if SI_Mode != 81:
            park.terminate()
            park.join()
            LED.terminate()
            LED.join()
            play.off_led()
            time.sleep(1)
            play.s_d()
            time.sleep(1)
            drive.start()
