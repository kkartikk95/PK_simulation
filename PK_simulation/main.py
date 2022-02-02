import time
import serial as serial
import GUI
ser = serial.Serial('COM4', 9600, timeout=5)
# U7U97ZS10I5A181490O6A0
def Serial():
    # ser = serial.Serial('COM4', 9600, timeout=5)
    ser.write(("/1ZR"+"\r").encode())
    test = ser.read(10)
    print(test)
    print(test[3])
    ser.close()

def status():
    print("------------------------------QUERYING STATUS OF THE PUMP------------------------------")
    # ser = serial.Serial('COM4', 9600, timeout=5)
    ser.write(("/1Q" + "\r").encode())
    resp = ser.read(10)
    print(resp[3])
    resp = resp[3]
    # ser.close()
    return resp


def initialization():
    print("------------------------------RUNNING INITIALIZATION----------------------------")
    # ser = serial.Serial('COM4', 9600, timeout=5)
    sts = status()
    while sts != 96:
        print("Waiting...")
        sts = status()
    ser.write(("/1U7U97ZR" + "\r").encode())
    resp = ser.read(10)
    print(resp[3])
    # ser.close()


def mediaprep():
    print("---------------------------MEDIA PREP STEP------------------------------")
    # ser = serial.Serial('COM4', 9600, timeout=5)
    sts = status()
    while sts != 96:
        print("Waiting...")
        sts = status()
    ser.write(("/1S23I4P1000,1R" + "\r").encode())
    sts = status()
    while(sts != 96 ):
        print("Aspirating 1ml from I4")
        sts = status()
    ser.write(("/1S24I3P1000,1R" + "\r").encode())
    sts = status()
    while (sts != 96):
        print("Aspirating 1ml from I3")
        sts = status()
    ser.write(("/1S27I2P500,1R" + "\r").encode())
    sts = status()
    while (sts != 96):
        print("Aspirating air")
        sts = status()



def cellculture():
    print("---------------------------FEEDING CELL CULTURE------------------------------------")
    # ser = serial.Serial('COM4', 9600, timeout=5)
    sts = status()
    while sts != 96:
        print("Waiting...")
        sts = status()
    ser.write(("/1S36O5D2000,1R" + "\r").encode())
    sts = status()
    while (sts != 96):
        print("Dispensing for culture")
        sts = status()
    ser.write(("/1S27O5D500,1R" + "\r").encode())
    sts = status()
    while (sts != 96):
        print("Dispensing air for culture")
        sts = status()
    ser.write(("/1S34I5P2000,1R" + "\r").encode())
    sts = status()
    while (sts != 96):
        print("Aspirating from culture")
        sts = status()
    ser.write(("/1S27I2P500,1R" + "\r").encode())
    sts = status()
    while (sts != 96):
        print("Aspirating air")
        sts = status()
    ser.write(("/1S36O6D500,1R" + "\r").encode())
    sts = status()
    while (sts != 96):
        print("Dispensing to sample")
        sts = status()


def cleanup():
    print("------------------------------CLEANING UP--------------------------------------")
    sts = status()
    while sts != 96:
        print("Waiting...")
        sts = status()
    ser.write(("/1S30O1D1500,1R" + "\r").encode())
    sts = status()
    while (sts != 96):
        print("Dispensing to waste")
        sts = status()
    ser.write(("/1S27O1D500,1R" + "\r").encode())
    sts = status()
    while (sts != 96):
        print("Dispensing to waste")
        sts = status()
    ser.write(("/1S27I2P500,1R" + "\r").encode())
    sts = status()
    while (sts != 96):
        print("Aspirating air")
        sts = status()
    ser.write(("/1S27O1D500,1R" + "\r").encode())
    sts = status()
    while (sts != 96):
        print("Dispensing for blowout to waste")
        sts = status()
    ser.write(("/1I3R" + "\r").encode())
    ser.close()

if __name__ == "__main__":
    # Serial()
    initialization()
    print("Initialization Done")
    mediaprep()
    print("Media Prep Done")
    cellculture()
    print("CellCulture Done")
    cleanup()
    print("CleanUP Done")
