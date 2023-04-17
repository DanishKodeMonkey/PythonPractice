'''
Lets play with the time module!
'''

#First things first, import the time module
import time

'''
Epoch
a date and time from which a computer measures system time.
    This code will call the time modules ctime function
    the ctime method converts a time expressed in seconds and convert it to a readable string.
    The argument 0 will make sure we take it from the actual epoch.
'''
print(time.ctime(0))
#Again, but this time 1 000 000 seconds from the time of the epoch
print(time.ctime(1000000))

print(time.time())