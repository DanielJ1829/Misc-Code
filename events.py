#events are things in python we can trigger
#when we trigger events we can react to them in the code
import threading
event = threading.Event() #we can either trigger or wait for this event
def myfunction():
    print("waiting for the event to trigger...")
    event.wait()  #waits until the event triggers or until event.set()
    print("Performing action z now...")

t1 = threading.Thread(target = myfunction)
t1.start()

x = input("Trigger event? (y/n)")
if x == "y":
    event.set() #triggers the event