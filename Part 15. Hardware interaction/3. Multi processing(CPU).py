'''
****************************
PYTHON MULTIPROCESSING
***************************
multi processing = running tasks in parallel on different cpu cores, by passes GIL used for threading
                    multiprocessing = better for cpu bound tasks(heavy cpu usage)
                    multithreading = better for io bound tasks(waiting around)

'''

from multiprocessing import Process, cpu_count
import time

def counter (num):      #we define a function called counter ,with a parameter called num
    count = 0           #the counter function creates a variable called count, which starts at 0
    while count < num:  #as long as count variable is less than the argument input to parameter num
        count += 1      #add 1 to count

def main(): #We define a function called main
    #We will first call the proccesing function cpu_count to tell us how many cores were
    #working with.
    print(cpu_count())
    '''
    Here we create a process called a, which targets the counter function
    And if we have arguments(which we do) we will pass them after a comma(,) seperated by commas(arg1,arg2)
    In this case we have one argument, and to differentiate this from an expression
    we end it with a comma(,) we have defined num as 1 billion in this case.
    '''
    a = Process(target=counter, args=(1000000000,)) #Create process a, which targets counter and counts to 500 mil
    b = Process(target=counter, args=(250000000,)) #Create process b, which targets counter, and counts to 500 mil
    c = Process(target=counter, args=(250000000,)) #Etc
    d = Process(target=counter, args=(250000000,)) #Etc
    a.start() #Start proccess a
    b.start() #start process b
    c.start() #ETC
    d.start() #ETC
    a.join() #wait for both process a-d to finish before starting main process
    b.join()
    c.join()
    d.join()
    #Print a counter with time.perf_counter() to see how long the counting took in the end.
    print("finished in: ",time.perf_counter()," seconds") #<----main process

    #HACKTOP TEST
    #CPU_count print = 4
    #in the first test using 1 process, to count to 1 billion, this took 161.94 seconds
    #in the second test, using 2 processes to count to 500 mil each, this took 166,94 seconds
    #in the third test, we used 4 processes to count to 250 mil each, this took 168.56 seconds

#if you find youself running 8 proccesses on a 4 processor CPU, you will find it
# might take longer than with 4, because creating and executing a process takes time
#but they wont be put into use since there is no core to assign them to.


#Windows oriented extra for safety.
#When we run a main process, and create a child process, the child process
#may create more child process, which can cause trouble.
#So we create this line so that when we create a child process
#it will copy our module without executing it

if __name__ == '__main__':
    main()