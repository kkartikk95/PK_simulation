import time
import serial as serial
from datetime import datetime
# ser = serial.Serial('COM4', 9600, timeout=5)
# f = open("logfile.txt", "a")
# now = datetime.now()
# U7U97ZS10I5A181490O6A0


def serial():
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
    print("------------------------------RUNNING INITIALIZATION----------------------------", file = f)
    # ser = serial.Serial('COM4', 9600, timeout=5)
    sts = status()
    while sts != 96:
        print("Waiting...")
        sts = status()

    ser.write(("/1U7U97ZR" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Pump Initialized", file = f)
    resp = ser.read(10)
    print(resp[3])
    # ser.close()


def mediaprep():
    print("---------------------------MEDIA PREP STEP------------------------------", file = f)
    # ser = serial.Serial('COM4', 9600, timeout=5)
    sts = status()
    while sts != 96:
        print("Waiting...")
        sts = status()

    ser.write(("/1S22I4P100,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirating 1ml from I4", file = f)
    sts = status()
    while(sts != 96 ):
        print("Aspirating 1ml from I4")
        sts = status()

    ser.write(("/1S22I3P1900,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirating 1ml from I3", file = f)
    sts = status()
    while (sts != 96):
        print("Aspirating 1ml from I3")
        sts = status()

    ser.write(("/1S21I2P500,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirating air from I2", file = f)
    sts = status()
    while (sts != 96):
        print("Aspirating air")
        sts = status()



def cellculture():
    print("---------------------------FEEDING CELL CULTURE------------------------------------", file = f)
    # ser = serial.Serial('COM4', 9600, timeout=5)
    sts = status()
    while sts != 96:
        print("Waiting...")
        sts = status()

    ser.write(("/1S23O5D2000,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing media to culture", file = f)
    sts = status()
    while (sts != 96):
        print("Dispensing for culture")
        sts = status()

    ser.write(("/1S23O5D500,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S")+ " " + "Dispensing Air to culture", file = f)
    sts = status()
    while (sts != 96):
        print("Dispensing air to culture")
        sts = status()

    ser.write(("/1S22I2P900,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirate air for culture", file=f)
    sts = status()
    while (sts != 96):
        print("Aspirate air")
        sts = status()

    ser.write(("/1S24O5D900,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing air for culture", file=f)
    sts = status()
    while (sts != 96):
        print("Dispensing air")
        sts = status()

    ser.write(("/1S23I5P2500,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirating old from culture", file = f)
    sts = status()
    while (sts != 96):
        print("Aspirating from culture")
        sts = status()

    ser.write(("/1S27O6D150,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing to Sample", file=f)
    sts=status()
    while (sts != 96):
        print("Dispensing to sample")
        sts = status()


def cleanup():
    print("------------------------------CLEANING UP--------------------------------------", file = f)
    sts = status()
    while sts != 96:
        print("Waiting...")
        sts = status()

    ser.write(("/1S21O1D2350,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing to waste", file=f)
    sts = status()
    while (sts != 96):
        print("Dispensing to waste")
        sts = status()

    ser.write(("/1S25I2P900,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirate air for sample blowout", file=f)
    sts = status()
    while (sts != 96):
        print("Aspirate air for sample")
        sts = status()

    ser.write(("/1S25O6D900,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing air for sample blowout", file=f)
    sts = status()
    while (sts != 96):
        print("Dispensing air for sample")
        sts = status()

    ser.write(("/1S22I2P800,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirating air for blowout", file = f)
    sts = status()
    while (sts != 96):
        print("Aspirating air")
        sts = status()

    ser.write(("/1S25O5D800,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing to culture blowout", file = f)
    sts = status()
    while (sts != 96):
        print("Dispensing for culture blowout")
        sts = status()

    ser.write(("/1I3R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Finished run", file = f)
    # ser.close()


if __name__ == "__main__":
    ser = serial.Serial('COM4', 9600, timeout=5)
    f = open("logfile.txt", "a")
    now = datetime.now()
    # Serial()
    # while(1):
    initialization()
    print("Initialization Done")
    mediaprep()
    print("Media Prep Done")
    cellculture()
    print("CellCulture Done")
    cleanup()
    print("CleanUP Done")
    time.sleep(30)
