from datetime import datetime
now = datetime.now()
f = open("testfile.txt","a")

print(now.strftime("%H:%M:%S") + " " + "hello", file =f)