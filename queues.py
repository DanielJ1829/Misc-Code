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
