import time
#Importing time in order to have the program wait a bit between executing code.
#for loop is a statement that will execute its block of code a limited amount of times.
#while loop is unlimited
#for loop is limited

#Example, for loop can be used to count to 10 for instance.
#To use a counter, people usually use index, or i for short.
#Statement below means "While index is in a range of 10, execute.
#In this example we simply execute what the index is at the time, +1 because computers start counting from 0
#The for loop in this example effectively execute 10 times.

#for i in range(10):
    #print(i+1)

#You can also count from a range of numbers by defining the start and end of the range. Adding a third statement will
#determine the steps taken, in this example each count will be by 2.
#for i in range(50,100+1,2):
#    print(i)

#A benefit of for statements is that it can itterate through anything itteratable, this goes for integers as well as strings

#Example. For i in whatever name it is, print each letter consecutively in a new line
#for i in "Daniel Runge":
#    print(i)

#Thanks to the imported time module we can now create a countdown that doesnt execute immediately.
#In this example we create a variable "seconds"(or i(index)) that have a range starting at 10, ending at 0, and counting backwards by -1
#and printing what seconds is by each itteration
#and using time.sleep() to pause the itteration for a second(1) between each itteration
#and finally, once the itteration reaches 0, it will execute the end, printing happy new year!
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy new year!")

