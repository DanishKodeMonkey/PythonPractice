#The return statement is a function that sends python values/objects back to the caller
#These values/objects are known as the functions return value.

#Define a function with the unique name multiply, with 2 parameters called number 1 and number 2.
def multiply(number1,number2):
    #define result as number 1 times(*) number 2
    result = number1 * number2
    #Tell Python to return the result
    return result

#Now we call the function, in order to actually display the result, we have to print the function.
print(multiply(6,8))


#Another use of this is to store the returned value within a variable

#Again, define a function with the unique name of multiply2, holding 2 parameters, number 21 and number22
def multiply2(number21,number22):
    #In the block of code, create a trigger called result2, which makes the program multiply number21 and number22
    result2 = number21 * number22
    #Return result2 to caller
    return result2

#Now define the variable to be the function call.
x = multiply2(6,8)

#And print the variable, which calls the function.
print(x)

