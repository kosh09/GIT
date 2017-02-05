import bluetooth
import serial
import struct
import play
import time
  
try:
    bd_addr = "98:D3:37:00:8D:39" # The address from the HC-05 sensor
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr,port))
except:
    play.bt_error()
    time.sleep(5)
    bd_addr = "98:D3:37:00:8D:39" # The address from the HC-05 sensor
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr,port))

play.bt_success()

try:
    ser = serial.Serial("/dev/ttyACM0", 57600)
except:
    play.serial_error()
    time.sleep(5)
    ser = serial.Serial("/dev/ttyACM0", 57600)

play.serial_success()

def DRIVING():
    while True:
        data = ord(sock.recv(1))
        string = ' '
        string = struct.pack('!B',data)
        ser.write(string)

def Mode_SIGNAL():
    while True:
        if data == 80:      # Driving mode
            return 80
        elif data == 81:    # Parking mode
            return 81
        else:
            return None

def LED_SIGNAL():
    while True:
        if data == 82:    # Turn  on LED or Laser
            return 82
        elif data == 83:    # Turn off LED or Laser
            return 83
        else:
            return None

def FR50():
    string = 59
    string = struct.pack('!B',string)
    ser.write(string)
def FR35():
    string = 62
    string = struct.pack('!B',string)
    ser.write(string)
def FR15():
    string = 65
    string = struct.pack('!B',string)
    ser.write(string)
def FS00():
    string = 68
    string = struct.pack('!B',string)
    ser.write(string)
def FL15():
    string = 71
    string = struct.pack('!B',string)
    ser.write(string)
def FL35():
    string = 74
    string = struct.pack('!B',string)
    ser.write(string)
def FL50():
    string = 77
    string = struct.pack('!B',string)
    ser.write(string)

def HR50():
    string = 60
    string = struct.pack('!B',string)
    ser.write(string)
def HR35():
    string = 63
    string = struct.pack('!B',string)
    ser.write(string)
def HR15():
    string = 66
    string = struct.pack('!B',string)
    ser.write(string)
def HS00():
    string = 69
    string = struct.pack('!B',string)
    ser.write(string)
def HL15():
    string = 72
    string = struct.pack('!B',string)
    ser.write(string)
def HL35():
    string = 75
    string = struct.pack('!B',string)
    ser.write(string)
def HL50():
    string = 78
    string = struct.pack('!B',string)
    ser.write(string)

def BR50():
    string = 61
    string = struct.pack('!B',string)
    ser.write(string)
def BR35():
    string = 64
    string = struct.pack('!B',string)
    ser.write(string)
def BR15():
    string = 67
    string = struct.pack('!B',string)
    ser.write(string)
def BS00():
    string = 70
    string = struct.pack('!B',string)
    ser.write(string)
def BL15():
    string = 73
    string = struct.pack('!B',string)
    ser.write(string)
def BL35():
    string = 76
    string = struct.pack('!B',string)
    ser.write(string)
def BL50():
    string = 79
    string = struct.pack('!B',string)
    ser.write(string)
