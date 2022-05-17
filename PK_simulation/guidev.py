from tkinter import *
import threading
import os
import subprocess


def p1():
    # os.system('python testpy1.py')
    threading.Thread(target=subprocess.run, args=(["python", "testpy1.py"],)).start()


def p2():
    # os.system('python testpy2.py')
    threading.Thread(target=subprocess.run, args=(["python", "testpy2.py"],)).start()

def p3():
    # os.system('python testpy2.py')
    threading.Thread(target=subprocess.run, args=(["python", "testpy3.py"],)).start()

def p4():
    # os.system('python testpy2.py')
    threading.Thread(target=subprocess.run, args=(["python", "testpy4.py"],)).start()


def test():
    pmpaddr = adr.get()
    if pmpaddr == 1:
        p1()
        # threading.Thread(target=call, args=("python testpy1.py" ,), ).start()
    if pmpaddr == 2:
        p2()
        # os.system('python testpy2.py')
    if pmpaddr == 3:
        p3()
    if pmpaddr == 4:
        p4()

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

start = Button(root, text="Start Program", command=test)
start.pack(side=LEFT, padx=210)

cancel = Button(root, text="Cancel Program")
cancel.pack(side=LEFT)

root.mainloop()
