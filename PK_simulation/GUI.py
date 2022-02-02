import tkinter

from tkinter import *
from tkinter import filedialog


def selectFile():
    filename = filedialog.askopenfilename(initialdir="/", title="Choose a file")
    file.insert(0, filename)
    fob=open(filename,'r')
    print(fob.read())

def logFile():
    filename = filedialog.askopenfilename(initialdir="/", title="Choose a file")
    log.insert(0, filename)
    fob=open(filename,'r')
    print(fob.read())


root = Tk()
root.title("IL-2 PK SIMULATION")
root.geometry("400x400")

file = Entry(root, width=45)
file.pack()
myButton = Button(root, text="Choose a CSV File", command=selectFile)
myButton.pack(pady=5)

log = Entry(root, width=45)
log.pack(pady=5)
button2 = Button(root, text="Select Log file", command=logFile)
button2.pack(pady=5)

adr = IntVar()
adr.set("Select Pump")
pumpaddr = OptionMenu(root, adr, 1, 2, 3, 4, 5, 6)
pumpaddr.pack(pady=5)

start = Button(root, text="Start Program")
start.pack()

cancel = Button(root, text="Cancel Program")
cancel.pack()

root.mainloop()

