import Laser_distance as LS
import time


while True:
    a = LS.distance_3()
    time.sleep(0.3)
    print("Distance from laser is ",a)
