import bluetooth
import serial
import struct

# Definition of Bluetooth rfcomm socket
bd_addr = "98:D3:37:00:8D:39" # The address from the HC-05 sensor
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))

# Definition of Serial port
ser = serial.Serial("/dev/ttyACM0", 57600)

def BT_DRIVING():
    while True:
        data = ord(sock.recv(1024))
        String = ' '
        String = struct.pack('!B',data)
        ser.write(string)

def BT_SIGNAL():
    while True:
        data = ord(sock.recv(1024))
        String = ' '
        String = struct.pack('!B', data)
        if String == 24:
            return 24
        elif String = 25:
            return 25:

def FR30():
    string = 10
    string = struct.pack('!B',string)
    ser.write(string)
def FR15():
    string = 11
    string = struct.pack('!B',string)
    ser.write(string)
def FS00():
    string = 12
    string = struct.pack('!B',string)
    ser.write(string)
def FL15():
    string = 13
    string = struct.pack('!B',string)
    ser.write(string)
def FL30():
    string = 14
    string = struct.pack('!B',string)
    ser.write(string)


def HR30():
    string = 15
    string = struct.pack('!B',string)
    ser.write(string)
def HR15():
    string = 16
    string = struct.pack('!B',string)
    ser.write(string)
def HS00():
    string = 17
    string = struct.pack('!B',string)
    ser.write(string)
def HL15():
    string = 18
    string = struct.pack('!B',string)
    ser.write(string)
def HL30():
    string = 19
    string = struct.pack('!B',string)
    ser.write(string)


def BR30():
    string = 20
    string = struct.pack('!B',string)
    ser.write(string)
def BR15():
    string = 21
    string = struct.pack('!B',string)
    ser.write(string)
def BS00():
    string = 22
    string = struct.pack('!B',string)
    ser.write(string)
def BL15():
    string = 23
    string = struct.pack('!B',string)
    ser.write(string)
def BL30():
    string = 24
    string = struct.pack('!B',string)
    ser.write(string)
