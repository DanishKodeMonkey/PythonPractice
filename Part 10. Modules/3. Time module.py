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

'''The time.time method, will return the current seconds since epoch'''
print(time.time())

'''
A way you can use the time module to retrieve the current date and time is
by combining both ctime and time in a print
'''

print(time.ctime(time.time()))
'''
so ctime will provide the amount of time since the computers epoch
and time.time will then convert c times return into a readable time and date
'''
'''
another way is to use the localtime method, which creates a localtime object.
which means we need to assign it a object name
'''
time_object = time.localtime()
print(time_object)
#Now if we print just this we will notice that the localtime prints
#the various different parts of the time and date in specific key:values
#which means we can pick and choose and format it in various ways! USEFUL!
'''so to convert this into a readable time, we can use strfttime function'''
'''The strftime function has two arguments
time.strftime(format, t)
t is just short for time_object ,which is what we generated above, so thats easy.
format is a string of different directives, which can be found on the documentation
of the function, good practise when in doubt is to read up on what and how
on such things: docs.python.org/3/library/time.html
in this example we will use %B(Month) %d(day) %Y(year) %H(hour)%M(Minutes)%S(Seconds)
assign all this to a variable called local_time
and print
'''
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)

print(local_time)

'''Final note, you can also get the UTC Coordinated Universal Time'''
#time_object = time.gmtime()

'''Next, we will play with the strp function
The strp function will parse a string representation of a time and date
and return a time object.
So we will need to pass in a string representating the date or time
as well as a format'''

#in our variable time string we litteraly just write some day and year
time_string = "20 April, 2020"
#We then assign those inputs to the time module with strptime
#This will then output as a time object, so we assign it all to a variable
#called time_object
time_object2 = time.strptime(time_string, "%d %B, %Y")
print(time_object2)
#Printing just this will once again print all of the functions outputs
#But notice how only the data we input is declared, rest is 0

'''Next is asctime
asctime accepts a time object, or a tuple representation of a relative time'''
#This time we will create a time tuple
#and use the time_tuple as argument for asctime, which will then return a time string
#which we assign by the same name.
#asctime reads the tuple as follows:
#year, month, day, hours, minutes, seconds, #day of the week, #day of the year, dst(daylight savings time 0/-1)
time_tuple = (2002, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

#If needed you can also use
# time.mktime(time_tuple)
#to convert the time to time-since-epoch

