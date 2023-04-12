# Args(Short for arguments) is a parameter that will pack all arguments into a tuple
#   This is useful so that a function can accept a varying amount of arguments

#As we know already, defining parameters in a function allows only that number of arguments to be input.

#def add(num1,num2):     #Having only 2 parameters in the function
#    sum = num1 + num2   #Allows only working with 2 arguments
#    return sum          #Adding more will result in an typeerror - position arguments

#print(add(1,2,3))


#In order to effectively allow any number of arguments we will use args
#args is not as important as the asterisk(*) infront of it, you can practically name it anything
#as long as it starts with the asterisk(*) to perform a packing into a tuple

def add(*args):         #Define function unique name add as any number of args(arguments) using asterisk(*)
    sum = 0             #The variable called sum will this time start at 0
    for i in args:      #For any i(index(itteration) written in args(asterisk(*))
        sum += i        #make the sum variable add(+) each itteration with the last
    return sum          #Return the result of this

print(add(1,2,3))       #Print the function add, with the arguments 1,2 and 3.
#This will effectively say 1+2+3 = 6
#Any amount of numbers can now be added and adjusted

#For the sake of confirming, *args does NOT need to be named args, you can name it anything and use it in the function
#Lets make the exact same program, but this time rename args to something else

def add2(*coffeemachine):       #Define a function with unique name add2 and open any number of arguments to a new parameter called coffeemachine
    sum = 0                     #A new variable is made, starting at 0
    for i in coffeemachine:     #For every index(itteration, value input) in coffeemachine
        sum += i                #add each number together in each itteration
    return sum                  #return the result of sum

print(add2(5,3,1,10))           #aand print

#So we effectively pack whatever arguments are input into a tuple, which are organised and unchangeable.
#This means we cannot change a index value, doing so will result in an error
#To make changes to the input values in the index, we need to convert it to a different collection
#This can be done via casting

def add3(*stuff):           #Define a function called add3, by making any number of arguments match a parameter called stuff
    sum = 0                 #Form a variable starting at 0
    stuff = list(stuff)     #Cast all the arguments in stuff as a list
    stuff[0] = 0            #Turn index 0(first value) into 0, so no matter what the first value is, it will be turn to 0
    for i in stuff:         #For each itteration in stuff
        sum += i            #Add new itteration to the last
    return sum              #Return the result of sum variable

print(add3(1,2,3,4,5,6))    #Since the first number is now 0, this says 0+2+3+4+5+6=20

#It is common naming convention to call it *args however