#semaphores limit access to the resource through a maximum value
#lets multiple but not unlimited resources access a module
import threading
import time
semaphore = threading.BoundedSemaphore(value=5) #allows 5 threads to access resource
# (or 5 accesses)

def access(thread_number):

    #:param thread_number: number of threads present
    #basic function that tries to access a resource

    print("{} is trying to access the resource".format(thread_number))
    semaphore.acquire() #acquires the resource
    print("{} was granted access.".format(thread_number))
    time.sleep(5) #waits 5s
    print("{} is now releasing...".format(thread_number))
    semaphore.release() #self explanatory

for thread_number in range(1, 11):      #pass the parameters into the function like this
    t = threading.Thread(target=access, args =(thread_number,))
    t.start()
    time.sleep(3) #pauses the code for a second for each loop'''