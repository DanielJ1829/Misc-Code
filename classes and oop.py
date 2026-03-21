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