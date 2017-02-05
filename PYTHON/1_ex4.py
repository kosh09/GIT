
# Import internal modules
import play
from multiprocessing import Process
import time

def one(a):                     # Definite Driving sequences
    print("server one")
    print('',a)
def two(a):
    print("server two")
    print('',a)
def three(a):
    print("server three")
    print('',a)
def four(a):                     # Definitie Parking sequences
    print("server four")
    print('',a)
def five(a):               # Alarm when parking is available
    print("server five")
    print('',a)
def six(a):                         # Blink Back LED
    print("server six")
    print('',a)
def seven(a):
    print("server seven")
    print('',a)

if __name__ == '__main__':
    b1b = Process(target = one,   args =('',))          # DRIVING Sequence
    b2b = Process(target = two,   args =('',))           # PARKING Sequence
    b3b = Process(target = three, args =('',))                # BLINKING LED
    b4b = Process(target = four,  args =('',))    # ALARM When Parking is Available
    b5b = Process(target = five,  args =('',))        # RECEIVE SIGNAL for Mode Selection
    b6b = Process(target = six,   args =('',))          # RECEIVE SIGNAL for LED
    b7b = Process(target = seven, args =('',))          # RING the Buzzer

    play.wel()
    time.sleep(1)

    b5b.start()
    time.sleep(1)

    play.alarm()
    time.sleep(1)

    play.s_p()
    b6b.start()
    b7b.start()

    while True:
        b1b.terminate()
        b1b.join()
        play.f_d()
        time.sleep(1)
        b2b.start()
        time.sleep(0.5)
        play.s_p()
        time.sleep(1)
        b3b.start()    # 주차 알고리즘에 주차가 끝났을때만 음악 재생되게 하고 시작재생은 여기서 하는걸로

        b3b.terminate()
        b3b.join()
        b2b.terminate()
        b2b.join()
        play.off_led()
        time.sleep(1)
        play.s_d()
        time.sleep(1)
        b1b.start()
