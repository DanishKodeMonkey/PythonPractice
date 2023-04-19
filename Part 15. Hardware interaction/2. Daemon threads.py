'''
Daemon Threads(CYBERPUNK BRRRRRR!)
A daemon thread is a thread that runs in the background,
and is not important for the program to run.
your program will not wait for daemon threads to complete before exiting

non-daemon threads cannot normally be killed, stay alive until task completes

ex. background tasks, garbage collection, waiting for input, long running proccesses
to name just a few.
'''

import threading
import time

#Here is an example of how daemon threads can be useful.
#We will have 2 threads.

#Our daemon thread will be working in the background, keeping track of how long the
#user has been online for. This will be done using a function:
def timer():              #We define a function called timer
    print()               #When the function is called, we print how long someone is logged in
    count = 0             #We do this by creating a count variable
    while True:                  #while True
        time.sleep(1)           #we will use the sleep function for 1 second
        count += 1              #We will then increment the count variable by 1
        print("logged in for: ", count, "seconds")  #and print the text here.

#now we create a daemon-thread to be in charge of the timer, and assign it.
'''
NOTE: If we use a non-daemon thread, the countdown timer WILL NOT stop after
the user inputs an exit command, this is because non-daemon threads cant be killed
So thread 1 will still be going despite the main thread being finished.
But the program will not end as long as there are non-daemon threads alive.
'''
#SO, to make a daemon thread, simply add the second argument daemon= True.
x = threading.Thread(target= timer, daemon= True)
#You can actually convert a thread to and from a daemon thread as long as its not running
#this is done with
#(thread name).setDaemon(True/False)
x.start()

#The main thread will be in charge of waiting around for some user input
answers = input("Do you wish to exit?: ")
