#threading
#threading allows us to speed up tasks by executing multiple things at once
#'lightweight' processes; need less resources compared to most processes
#multiple threads in the same process share the same memory space
#allows for better communication and synchronisation
import threading
import time
def helloworld():
    print("Hello World!")

def function1():
    for x in range(10000):
        print("one")
def function2():
    for x in range(10000):
        print("two")

t0 = threading.Thread(target=helloworld) #not helloworld() as we're just referring to the function, not executing/calling it
#.Thread is a class, target is the object
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)  #allows both to execute simulatneously
#could use this to compare algorithmic complexity of prime sieves

#-------------------------------------------------- run either the code above ^^ or the code below \/ \/

t1.start()
t2.start()

def hello():
    for x in range(50):
        print("Hello!")

t1 = threading.Thread(target=hello)
t1.start() #this script is already in a main thread
#main thread already running; every thread that starts is already in this thread

t1.join() #this orders the code by line, executing the functions before the print statement below

print("Another Text") #this prints before the 50 "Hello!"'s despite is being above in the code UNLESS you have t1.join beforehand