#what is going on guys and welcome to this python tutorial series for intermediates
#in today's episode we're going to talk about a concept which is actually not that intermediate is actually quite fundamental but we haven't talked about it yet
#the topic is called recursion

#recursion - technique of a function calling itself in the code eg f1(f1())
#you don't want an endless loop, this creates a 'stack overflow' (where it got its name)

#factorial function: 9! = 9*8*7*6*5*4*3*2*1
#9! = 9*8!, (n+1)! = (n+1)*n!

#non recursive way
n = 7
fact = 1
while n > 0:
    fact = fact*n
    n -= 1
print(fact)
#recursive way
def factorial(n):
    if type(n) != int or n < 0:
        raise ValueError("You need to enter a positive integer for the factorial function to work")
    if n == 0:
        return 1  #yikes, in reality I want if n = 0 here but would need a better validation system
        #note: once the function has returned one (reached n=0)
        # it stops returning, so by the time you get to n=1,
        #you have factorial(0) below \/ so it just returns one and exits the functtion
    else:
        number = n * factorial(n-1)  #once you get to 0, it returns 1 then continues returning 1
        return number

print(factorial(7))

def fibonacci(n):
    n_0 = 0  #the first fibonacci number
    n_1 = 1  #the second fibonacci number
    x = 1
    while x <= n-1:
        y= n_0 + n_1
        n_0 = n_1
        n_1 = y
        x += 1
    return y

def fibonacci2(n): #more efficient code for it
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a

def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1)+fib_recursive(n-2) #this has 2^n order, every time you call the function, it has to call
                                                    #2 functions, which each have to call 2 functions and so on
#if you..
import time
#then do:
t1 = time.time()
x = fib_recursive(40)
t2 = time.time()
print(x, 'time taken: {}'.format(t2-t1))

t3 = time.time()
x = fibonacci(40)
t4 = time.time()
print(x, 'time taken: {}'.format(t3-t4))

t5 = time.time()
x = fibonacci2(40)
t6 = time.time()
print(x, 'time taken: {}'.format(t5-t6))
#you get this:
# 102334155 time taken: 13.312607288360596
# 102334155 time taken: -9.775161743164062e-06
# 102334155 time taken: -1.4543533325195312e-05 so the second method is just slower than
#the one i designed initially but you can see how massive the difference is here
#therefore you have to think about the order of recursion functions first b4 implementing it