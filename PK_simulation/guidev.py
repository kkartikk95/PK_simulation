from tkinter import *
import threading

def test():
    pmpaddr = adr.get()


root = Tk()
root.title("IL-2 PK SIMULATION")
root.geometry("800x800")

file = Entry(root, width=45)
file.pack()
myButton = Button(root, text="Choose a CSV File")
myButton.pack(pady=20)

log = Entry(root, width=45)
log.pack(pady=5)
button2 = Button(root, text="Create log file")
button2.pack()

adr = IntVar()
adr.set("Select Pump")
pumpaddr = OptionMenu(root, adr, 1, 2, 3, 4, 5, 6)
pumpaddr.pack(pady=10)

start = Button(root, text="Start Program")
start.pack(side=LEFT, padx=210)

cancel = Button(root, text="Cancel Program")
cancel.pack(side=LEFT)

root.mainloop()
