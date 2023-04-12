#An Exception is an event that is detected during execution that interrupts the flow of a program

#To illustrate, we will create a simple division program
#And try to handle exceptions before they cause an exception and interrupt the program
#Correction lines will be define by a #--
#A very basic form of handling potential exceptions, is to surround any
#code that is considered dangerous, as in it might cause an exception
#inside a try block.
# generally any user input shoudl be considered potentially dangerous

try:                                                            #--Add a try function here to wrap the code in a exception block
    numerator = int(input("Enter a number to divide: "))        #Define a variable, called numerator, determined in the form of a integer, input from the user
    denominator = int(input("Enter a number to divide by: "))   #Define a variable, called denominator, determined in the form of a integer, input from the user
    result = numerator / denominator                            #Define a variable, called result, that is the division of the numerator and denominator variable
        #note how there has been no print of result, see below

#It is generally good practise to define several exception blocks for specifific exceptions
#To tell the program how to handle specific issues instead of just "HANDLE ALL ISSUES IN ONE WAY ONLY!
#Common good practise is to also print the actual exception error,
# this is done by creating the exception block as e(for exception) and printing e
except ZeroDivisionError as e:                                       #To catch a specific exception, write the name of the exception
    print(e)
    print("You cant divide by zero! Silly!")                    #Then write whatever the program should do instead! Like a message.
except ValueError as e:                                              #Again, catch a specific exception, like ValueError whenever a letter or something NOT a numberi s used
    print(e)
    print("Enter only numbers!")                                  #And print a explanation instead of a interruption!
except Exception as e:                                               #To catch the exception we will form a except block which will catch ANY exception.
    print(e)
    print("Something went wrong :(")                            #Now, whenever any exception is caught, that is otherwise not defined, we will instead print this.
else:                                                           #Should NONE of the exceptions above occour, then we can do below instead.
    print(result)                                               #now, finally ,should no exceptions occour, we can print
finally:                                                        #finally function will always happen no matter what
    print("This will always execute")                           #Usually used to close a opened file, in this case we will just print.
#Normally this would work just fine, but if someone intentionally causes an error, by dividing by 0 for instance
#which is mathematically impossible, it will result in an exception.
#This will result in the program being interrupted.

