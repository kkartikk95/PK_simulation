from tkinter import *
from tkinter import filedialog
import tkinter as tk
import dataimport
import pumpA1
# global filename
# global fe


def selectFile():
    global filename
    filename=filedialog.askopenfilename(initialdir="/", title="Choose a file")
    file.insert(0, filename)
    #fob=open(filename,'r')
    #print(fob.read())


def logFile():
    logger = log.get()
    global fe
    fe = str("" + logger + ".txt")
    #txtfile = open(fname, "w")
    return fe


def pump_program():
    global fe
    pmpaddr=adr.get()
    mediaA11, mediaA12, mediaA21, mediaA22, mediaA31, mediaA32, mediaB11, mediaB12, mediaB21, mediaB22, mediaB31, mediaB32 = dataimport.datafunc(filename)
    if pmpaddr == 1:
        pumpA1.main(fe, mediaA11, mediaA12)



if __name__ == "__main__":
    root = Tk()
    root.title("IL-2 PK SIMULATION")
    root.geometry("800x800")

    file = Entry(root, width=45)
    file.pack()
    myButton = Button(root, text="Choose a CSV File", command=selectFile)
    myButton.pack(pady=20)

    log = Entry(root, width=45)
    log.pack(pady=5)
    button2 = Button(root, text="Create log file", command=logFile)
    button2.pack()
    lbl = Label(root, text="Don't add .txt, just type the name")
    lbl.pack()

    adr = IntVar()
    adr.set("Select Pump")
    pumpaddr = OptionMenu(root, adr, 1, 2, 3, 4, 5, 6)
    pumpaddr.pack(pady=10)

    lbl1 = Label(root, text="NOTES:\n"
                            "1. Remember to add CSV file.\n"
                            "2. Give the log file a name do not add .txt to file name. That will happen automatically\n"
                            "3. Press the create log file button after giving the name\n"
                            "4. Pump address for now is 1 rest will be added soon\n"
                            "5. Once the program starts it will not stop. Will add functionality in upcoming versions\n"
                            "6. Runtime is 18 mins for testing purposes now\n"
                            "7. Log files and software files will located in C:\Users\grobot\Documents\GUI folder\n"
                            "8. Test csv file for media volumes is in desktop named as test.csv")
    lbl1.pack(pady=5)
# for testing purposes only
#     button3 = Button(root, text="test", command=runextra)
#     button3.pack(pady=20)

    start = Button(root, text="Start Program", command=pump_program)
    start.pack(side=LEFT, padx=210)

    cancel = Button(root, text="Cancel Program")
    cancel.pack(side=LEFT)

    root.mainloop()

