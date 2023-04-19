'''So to start, what is threading?'''
'''
Think of threading as a flow of execution, like a flowing river
It is like a seperate order of instructions
    However, each thread takes a turn running to achieve concurrency
    GIL = (Global Interpreter Lock)
    and allows only ONE thread to hold the control of the python interpreter at any one time
    
cpu bound = program/task spends most of it's time waiting for internal events(CPU intensive)
it is better to use multiprocessing in this case

io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
it is better to use multithreading
'''
#Importing the threading module allows us to count the number of threads currently running
import threading
import time

#threading.active_count, as the name suggests, will return the number of threads currently active
    #print(threading.active_count())
#threading.enumerate, will return WHICH thread is currently running
    #print(threading.enumerate())

#so the basis of using multi threading would be to seperate the workload across
#multiple threads, having the main thread working on the main body program
#while a seperate thread works on a seperate program.

'''
An example of a io bound multithreading purpose
could be for the quizgame, while waiting for the user input, which the main thread
is handling
have another thread handle a supposed timer countdown to tell the user that they
are running out of time!
'''

'''
For this example however, we will make a program that will run multithreading
We are late for school and we have 3 tasks we have to do before we can go.
each of these tasks will take a given amount of seconds to complete
'''

def eat_breakfest():
    time.sleep(3)
    print("You eat breakfest")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You study")

'''
we will simulate this with a time-sleep function
Each of the below tasks are I/O bound, they spend alot of time waiting for external events.
They are waiting for the sleep function to expire before they finish their task
'''
'''Now we will run the script and see how long it takes us to complete the morning ritual'''

# eat_breakfest()
# drink_coffee()
# study()

'''This program took about 12 seconds overall
We completed these tasks sequencially instead of consecurently'''

'''
Currently we have one thread taking care of all 3 functions.
We can instead assign one thread for each function.
Effectively eating breakfest, drinking coffee, and studying at the same time
some kind of super hero multi tasking
'''

'''
To do this we do the following:
'''
#First we define a new thread, naming it x.
#The thread is created with threading.thread, assigned a function(eat_breakfest)
#and if applicaple, arguments are input with args, divided by commas(,)
x = threading.Thread(target= eat_breakfest, args=())
#Then, to begin the thread, we type:
x.start()
#Lets do this again with the other functions
y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

#NOTE: Remember to call the funciton in target WITHOUT () or it wont work! arguments go
#seperately!
'''Now when we execute the program, 3 different threads handle the 3 tasks 
at the same time, while looking up the active thread count and each
threads purpose. 
Aaand BOOM, it took 5 seconds, which is the timer of the htird function'''
#There is a concept called thread synchronisation
#We have a calling thread, to wait around for another thread to finish, before it begins.
#To do this, have the thread call a funciton called join.
x.join()
y.join()
z.join()
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
#NOTE: The print of the thread active_count and enumerate was run on the main thread
#which wont wait around for the other threads to work, and finish its task before
#thread 1, 2, and 3.