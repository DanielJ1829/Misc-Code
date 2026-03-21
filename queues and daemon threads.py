import threading
import time

#daemon threads run in the background, the script can terminate even whilst daemon threads
#are still running
#eg you could use this for constantly reading in information from a file or script

path = "To Do List"
text = ""
def readFile():
    global path, text
    while True:
        with open("To Do List", "r") as f:
            text = f.read()
        time.sleep(3)
def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target = readFile, daemon=True)
t2 = threading.Thread(target=printloop)
t1.start()
t2.start()   #i can edit the text file WHILST the code is actually running and it will print the updated file
#amidst editing it; this could allow for some pretty interesting stuff should we not just be printing things here
#eg updating a new file based off how one file behaves(eg weather data or so on)