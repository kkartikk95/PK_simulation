import serial as serial
import time
import GUI

def main():
    ser = serial.Serial('COM4', 9600, timeout=5)
    ser.write(("/1ZS22P1000,1R" + "\r").encode())
    time.sleep(15)
    ser.write(("/1T" + "\r").encode())
    resp = ser.read(10)
    print("Og resp", resp)
    while resp[3] != 96:
        ser.write(("/1Q" + "\r").encode())
        resp = ser.read(10)
    ser.write(("/1?1" + "\r").encode())
    resp = ser.read(10)
    x = resp[4:9]
    print(x.decode("utf-8"))
    var = x.decode("utf-8")
    GUI.textbox(var)
    reset = x.decode("utf-8")
    while resp[3] != 96:
        ser.write(("/1Q" + "\r").encode())
        resp = ser.read(10)
    reset = str(reset)
    ser.write(("/1O1D"+reset+"R" + "\r").encode())