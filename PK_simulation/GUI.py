from tkinter import *
from tkinter import filedialog
import dataimport
import pumpA1
global filename
global fname

def selectFile():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Choose a file")
    file.insert(0, filename)
    #fob=open(filename,'r')
    #print(fob.read())
    return filename

def logFile():
    logger = log.get()
    global fname
    fname = str("" + logger + ".txt")
    #txtfile = open(fname, "w")
    return fname

def pump_program():
    pmpaddr=adr.get()
    mediaA11, mediaA12, mediaA21, mediaA22, mediaA31, mediaA32, mediaB11, mediaB12, mediaB21, mediaB22, mediaB31, mediaB32 = dataimport.datafunc(filename)
    if pmpaddr == 1:
        pumpA1.main(fname, mediaA11, mediaA12)


if __name__ == "__main__":
    root = Tk()
    root.title("IL-2 PK SIMULATION")
    root.geometry("400x400")

    file = Entry(root, width=45)
    file.pack()
    myButton = Button(root, text="Choose a CSV File", command=selectFile)
    myButton.pack(pady=5)

    log = Entry(root, width=45)
    log.pack(pady=5)
    button2 = Button(root, text="Log file name", command=logFile)
    button2.pack(pady=5)

    adr = IntVar()
    adr.set("Select Pump")
    pumpaddr = OptionMenu(root, adr, 1, 2, 3, 4, 5, 6)
    pumpaddr.pack(pady=5)

    start = Button(root, text="Start Program", command=pump_program)
    start.pack()

    cancel = Button(root, text="Cancel Program")
    cancel.pack()

    root.mainloop()

