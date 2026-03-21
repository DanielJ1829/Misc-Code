import numpy as np
import matplotlib.pyplot as plt
'''name = input('state your name cuz: ')
#while loops - repeat blocks of code for the duration a condition holds
# rechecks the condition at the end of each loop
while name == '':
    name = input('enter your name: ')
age = int(input('enter your age: '))
while age < 0:
    print("age can't be less than 0")
    age = int(input("enter your age: "))
print(f"Hello {name}!")
print(f"good to know that you're {age} years old")'''
'''#for loops: used to iterate over a given sequence (string, list, tuple, set)
# repeat a clode block for an exact amount of times

#for x in range(91,103, 2):    #range(initial number, ending number -1, step between) - they need to be integers
#    print(x)
import time

name = str(input('enter a word or sentence: '))
for letter in name:
    print(letter, end="!")

for i in range(10, 0 , -1):
    print(i)
    time.sleep(1)
#escape loop:
print('end of countdown')'''
'''lists: [] - mutable (), most flexible
alph = ['a', 'b', 'c', 'd']
for letters in alph:
    print(letters, end = ' ')
alph.pop(1)   #- .pop() gets rid of a specific element of the list
print(alph)  # shows the list without b in it; now alph[3] doesn't exist, alph[2] is now instead d not c'''
'''Tuples: () - immutable, faster
fruits = ("apple", "orange", "banana", "coconut")
#fruits.append #or .pop() etc aren't possible as tuples are immutable (u get an error if you un hashtag this line)
#they're good if you need a collection that can't be changed in any way
#also can't use .remove(), .clear()'''
'''Sets {} - mutable, unordered, no duplicates, best for membership testing
#most complicated
import numpy as np
numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

i = 0
while i < 5:
    for number in numbers:
        print(number, end=" ")
    i += 1  #this block of code shows that every time you rerun it, the order of numbers is different, but constructing a while loop
    # just reprints out the same randomly generated order from before 5 times. To do pseudorandom generation we'd have to do something else (what??)
numbers.add("11") #-> inserts 11 randomly into the set since it is not ordered
list = []
for number in numbers:
    list.append(number)
list = list[0:5:1]
print(list)  #this block of code allows me to extract a list of 5 randomly selected numbers using sets' unordered property'''
'''def factorise_number(x):
    while True:
        n = input('enter a number to factorise:').strip()
        try:
            n = int(n)
            break
        except ValueError:
            print('Please enter an integer')
        try:
            n < x**2
            break
        except ValueError:
            print("Please enter an integer smaller than the upper bound's square root.")
    factors = []
    for i in np.arange(0, len(primes), 1):
        if n%primes[i] == 0:
            factors.append(primes[i])
        else:
            pass
    if len(factors) == 0:
        print('this number is prime')
    else:
        print('this number has prime factors {}'.format(factors))
    return factors'''
'''x = np.linspace(-10, 10, 101)
y = np.linspace(-10, 10, 101)

xx, yy = np.meshgrid(x, y)
zz = np.sqrt(xx**2 + yy**2)

#xs, ys = np.meshgrid(x,y, sparse = True)
#zs = np.sqrt(xs**2 + ys**2)
h = plt.contourf(x, y, zz)
#plt.axis('scaled')
#plt.colorbar()
plt.show()
x = np.linspace(-5, 5, 101)
y = np.linspace(-5, 5, 101)
# full coordinate arrays
xx, yy = np.meshgrid(x, y)
zz = np.sqrt(xx**2 + yy**2)
#xx.shape, yy.shape, zz.shape
#((101, 101), (101, 101), (101, 101))
# sparse coordinate arrays
xs, ys = np.meshgrid(x, y, sparse=True)
zs = np.sqrt(xs**2 + ys**2)
#xs.shape, ys.shape, zs.shape
#((1, 101), (101, 1), (101, 101))  -technically redundant code
h = plt.contourf(x, y, zs)   #contourf fills this out
plt.axis('scaled')
plt.colorbar()
plt.show()

xs, ys = np.meshgrid(x, y, sparse=True)
print(xs)'''
'''def day_of_week(day):
    match day:
        case 1:
            return 'It is Monday'
        case 2:
            return 'It is Tuesday'
        case 3:
            return 'It is Wednesday'
        case 4:
            return 'It is Thursday'
        case 5:
            return 'It is Friday'
        case 6:
            return 'It is Saturday'
        case 7:
            return 'It is Sunday'
        case _:
            return 'Not a valid day''' #match casing
'''def day_of_week(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in np.arange(0, len(days), 1):
        match day:
            case i:
                return f'It is {days[i-1]}' ''' #''
'''def day_of_week(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    try:
        for i in np.arange(0,len(days), 1):
            match day:
                case i:
                    return f'It is {days[i-1]}'
    except:
            return 'Not a valid day'
''' #''

class Person:  #a class is an object constructor

    amount = 0  #this is a class variable

    def __init__(self, name, age, height):    #constructor; initialises a new object when Person() is called
        self.name = name  #attributes, also known as instance variables
        self.age = age
        self.height = height  #Generally, it's considered better design to keep user input separate from logic which is why we do this here instead of input()
        Person.amount += 1  #shows more ppl happening

    def helloWorld(self):   #this is known as an instance method (or method); tied to a specific object, and accessed like x.helloWorld()
        print('hello world')

    def __del__(self):
        Person.amount -= 1  #removes 1 from amount of ppl (shocker)

    def __str__(self):  #gives you something to print if you don't do person1.something and just do print(person1) this is a *string representation*
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)  #if u do return "Bullshit", doing print(Person1) returns Bullshit

    def get_older(self, years):
        self.age += years

class Worker(Person):  #this is known as a 'child class' whilst the Person class is a parent class
    def __init__(self, name, age, height, salary):  #super() accesses the parent class (person)
        super(Worker, self).__init__(name, age, height) #allows us to access init constructor of the parent class and use it here  (inheritance)
        self.salary = salary

    def calc_yearly_salary(self):
        return self.salary*12

    def __str__(self):
        text = super(Worker,self).__str__()   #again, this is inheritance using the previous string func from the parent class
        text += ", Salary: {}".format(self.salary)
        return text

worker1 = Worker("Philip", 40, 180, 3000)


Person1 = Person("Mike", 21, 193)   #person1 is an object
print(Person1.name)
Person1.height = 188
Person1.age = 25
print(Person1.age, Person1.name, Person1.height)
Person1.helloWorld()
print(Person1)
person2 = Person("Sara", 25, 163)
print(Person.amount)
del Person1  #deletes the object Person1

#user defined operator overloading: define yourself what happens when you apply any operator to two objects

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __str__(self):
        return "X: {}, Y: {}, Z: {}".format(self.x, self.y, self.z)

    def __iter__(self):
        self.a = self.x  # or 1 or whatever; these allow you to iterate inside of a class and a bit more efficiently
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x

v1 = Vector(2,5,8)
v2 = Vector(6,3,15)
v3 = v1 - v2
print(v3)
h = Vector(1,1,1)
myit  = iter(v1)

for i in range(10):
    print(next(myit))  #classes, inheritance and iterators
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
#locking controlling the flow of different threads in the same memory space. Lock, Lock.acquire()/release()
#allows one thread at a time to access the resource (here, x is the resource (the global variable)
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

#semaphores limit access to the resource through a maximum value
#lets multiple but not unlimited resources access a module

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
#events and daemon threads
#events are things in python we can trigger
#when we trigger events we can react to them in the code
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


#queues
#similar to lists and sequences however have a specific order of how elements get into the list
#and how we can access them to get them out of this list

#when we have multiple threads running, you need to have a good/structured way of
#retrieving/writing data due to the unordered nature of multithreading
#queues remove elements or pop elements that have been operated on
#having multiple threads accessing the same queue will mean each thread will just get
#the next element in the queue, in spite of multiple threads acting on the queue
#eg if thread 4 takes out a, the next available element for any of the threads to act on is b
#then after b's been taken out, the next available thread will take out c and so on

import queue
q = queue.Queue()
list  = ["a", "b", "c", "d", "e", "f", "g", "h"]


for i in list:
    q.put(i) # taking all elements of the list and putting them in a queue
for j in range(len(list)):
    print(q.get())

#this is a first in first out queue

q = queue.LifoQueue() #this is a last in first out queue
numbers = [1,2,3,4,5,6,7,8,9]
for x in numbers:
    q.put(x)
print(q.get()) #returns the last element of the list

q = queue.PriorityQueue()
#allows you to give each element a certain priority, using/passing a tuple
q.put((2, "Hello World"))
q.put((11, 99))
q.put((5, "yo my slime"))
q.put((1, 4.5))
while not q.empty():
    print(q.get()) #shows us key-value pairs in order of priority. can do q.get()[1] to get just the values


