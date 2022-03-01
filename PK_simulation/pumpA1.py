import time
import serial as serial
from datetime import datetime
# ser = serial.Serial('COM4', 9600, timeout=5)
# f = open("logfile.txt", "a")
# now = datetime.now()
# U7U97ZS10I5A181490O6A0

# def serial():
#     # ser = serial.Serial('COM4', 9600, timeout=5)
#     ser.write(("/1ZR"+"\r").encode())
#     test = ser.read(10)
#     print(test)
#     print(test[3])
#     ser.close()


def status(ser):
    print("------------------------------QUERYING STATUS OF THE PUMP------------------------------")
    # ser = serial.Serial('COM4', 9600, timeout=5)
    ser.write(("/1Q" + "\r").encode())
    resp = ser.read(10)
    print(resp[3])
    resp = resp[3]
    # ser.close()
    return resp


def initialization(f, ser):
    print("------------------------------RUNNING INITIALIZATION----------------------------", file=f)
    # ser = serial.Serial('COM4', 9600, timeout=5)
    sts = status(ser)
    while sts != 96:
        print("Waiting...")
        sts = status(ser)

    ser.write(("/1U7U97ZR" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Pump Initialized", file=f)
    resp = ser.read(10)
    print(resp[3])
    # ser.close()


def mediaprep(f, ser, ma1, ma2):
    print("---------------------------MEDIA PREP STEP------------------------------", file=f)
    # ser = serial.Serial('COM4', 9600, timeout=5)
    sts = status(ser)
    while sts != 96:
        print("Waiting...")
        sts = status(ser)

    ser.write(("/1S22I4P"+ma1+",1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirating "+ma1+" from I4", file=f)
    sts = status(ser)
    while(sts != 96):
        print("Aspirating 1ml from I4")
        sts = status(ser)

    ser.write(("/1S22I3P"+ma2+",1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirating "+ma2+" from I3", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Aspirating 1ml from I3")
        sts = status(ser)

    ser.write(("/1S21I2P500,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirating air from I2", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Aspirating air")
        sts = status(ser)


def cellculture(f, ser):
    print("---------------------------FEEDING CELL CULTURE------------------------------------", file=f)
    # ser = serial.Serial('COM4', 9600, timeout=5)
    sts = status(ser)
    while sts != 96:
        print("Waiting...")
        sts = status(ser)

    ser.write(("/1S23O5D2000,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing media to culture", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Dispensing for culture")
        sts = status(ser)

    ser.write(("/1S23O5D500,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing Air to culture", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Dispensing air to culture")
        sts = status(ser)

    ser.write(("/1S22I2P900,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirate air for culture", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Aspirate air")
        sts = status(ser)

    ser.write(("/1S24O5D900,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing air for culture", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Dispensing air")
        sts = status(ser)

    ser.write(("/1S23I5P2500,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirating old from culture", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Aspirating from culture")
        sts = status(ser)

    ser.write(("/1S27O6D150,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing to Sample", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Dispensing to sample")
        sts = status(ser)


def cleanup(f, ser):
    print("------------------------------CLEANING UP--------------------------------------", file=f)
    sts = status(ser)
    while sts != 96:
        print("Waiting...")
        sts = status(ser)

    ser.write(("/1S21O1D2350,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing to waste", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Dispensing to waste")
        sts = status(ser)

    ser.write(("/1S25I2P900,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirate air for sample blowout", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Aspirate air for sample")
        sts = status(ser)

    ser.write(("/1S25O6D900,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing air for sample blowout", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Dispensing air for sample")
        sts = status(ser)

    ser.write(("/1S22I2P800,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Aspirating air for blowout", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Aspirating air")
        sts = status(ser)

    ser.write(("/1S25O5D800,1R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Dispensing to culture blowout", file=f)
    sts = status(ser)
    while (sts != 96):
        print("Dispensing for culture blowout")
        sts = status(ser)

    ser.write(("/1I3R" + "\r").encode())
    now = datetime.now()
    print(now.strftime("%H:%M:%S") + " " + "Finished run", file=f)
    # ser.close()


def main(logfile, mediaA11, mediaA12):
    ser = serial.Serial('COM4', 9600, timeout=5)
    f = open(logfile, "a")
    now = datetime.now()
    # Serial()
    # while(1):
    x = len(mediaA11)
    y = len(mediaA12)
    if x == y:
        ma1 = str(mediaA11[0]*1000)
        ma2 = str(mediaA12[0]*1000)
        print("Media A volume: "+ma1+" ml\nMedia B volume: "+ma2+" ml\n", file=f)
        initialization(f, ser)
        print("Initialization Done")
        mediaprep(f, ser, ma1, ma2)
        print("Media Prep Done")
        cellculture(f, ser)
        print("CellCulture Done")
        cleanup(f, ser)
        print("CleanUP Done")
        time.sleep(30)

