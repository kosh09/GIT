
# Import other python files
import Bluetooth&Serial as DRIVE
import Parking_algorithm as Park
import Laser_distance as Laser
import Ultrasonic_distance as Ult
import play_wav_file as WAV
import LED_BLINK as LED

# Import internal modules
import serial
import time
import bluetooth
import serial
import struct

def driving():                      # Definite Driving sequences
    DRIVE.BT_DRIVING()
def parking():                      # Definitie Parking sequences
    Park.Parking()
def alarm_parking():                # Alarm when parking is available
    Park.Alarm()
def LED():                          # Blink Red light while parking
    LED.Blink()

value = DRIVE.BT_SIGNAL()           # Return the value 25 or 26 from bluetooth

if __name__ == '__main__':
    drive = Process(target = driving)
    park = Process(target = parking)
    Led = Process(target = LED)
    Alarm = Process(target = alarm_parking)

    while True:
        if value == 25:             # Driving sequence is begin
            park.terminate()
            Led.terminate()
            time.sleep(1.5)
            Alarm.start()
            Alarm.join()
            drive.start()
            drive.join()
        elif value == 26:           # parking sequence is begin
            drive.terminate()
            Alarm.terminate()
            time.sleep(1.5)
            Led.start()
            Led.join()
            park.start()
            park.join
