#locking controlling the flow of different threads in the same memory space. Lock, Lock.acquire()/release()
#allows one thread at a time to access the resource (here, x is the resource (the global variable)
import threading
import time
x = 8192
#global says we want the global x variable inside of our function so we can manipulate it

lock = threading.Lock()  #lock is part of threading module, allows/forbids us to access a resource

def double():
    global x, lock
    lock.acquire() #tries to acquire lock if it's free -> if another function/thread has already locked a resource it can't be locked again
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1) #tells program to wait for 1 (or x generally) second (s)
    print("Reached the maximum")
    lock.release()

def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum")
    lock.release()

t1 = threading.Thread(target = halve)
t2 = threading.Thread(target = double)
t1.start()
t2.start()
