#Nested Function Calls  are function calls inside other function calls
#                       innermost function calls are resolved first
#                       returned value is used as argument for the next outer function

#Example 1, finding a positive number through a series of functions
print("Finding a positive number through a series of functions")
num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

#This will prompt the user to enter a whole positive number, should the user not do this the program
#will immediately 1. convert the input to a floating point umber(decimal),
#2. Find the absolute value(how far the value is from 0) from num
#3. round num to the nearest whole number
#4. and then print the result


#Example 2, same result, with nested function calls
#First we start with the user input, the first function that all the nested functions will wrap around
#Going in order of what we did above, we add a float function to the input function by wrapping it around it.
#The program will then execute from the innermost input function, resolving the functions one by one
# until reaching the outermost print function
#all in one line!

print("Find a positive number through nested function calls")
print(round(abs(float(input("Enter a whole positive number: ")))))

