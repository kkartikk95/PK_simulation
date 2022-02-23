import serial as serial
from datetime import datetime
ser = serial.Serial('COM4', 9600, timeout=5)

ser.write(("/1ZS20O1D2500,1R" + "\r").encode())