'''
Higher order function = a function that either:
    1. Accept a function as an argument
    2. returns a function as an output
    (In python, functions are also treated as objects)
'''

#Example of number 1:
#We will first define 2 functions:
def loud(text):         #We define a function called loud, that accepts a value called text
    return text.upper() #The function will return the text value all in uppercase as an output

def quiet(text):        #We define a function called quiet, that accepts a value called text.
    return text.lower() #The function will return the text value all in lowercase as an output.

#Now we define a third function, hello, which will be the higher order function
#it will accept a function as an argument, in this case func

def hello(func):            #So we define a new function called hello, that accepts a argument in the form of a function.
    text = func("Hello")    #Now we create a variable called text, that calls the func argument and assign it to the string "hello"
    print(text)             #and print the result.

#Now we can call either the loud, or quiet function using the hello function.

#These will then call both HELLO and hello
hello(loud)
hello(quiet)

'''
What happens is essnentially this:
Were calling the hello function with hello(loud).
    -->We parsing in the "loud" function as an argument
       were "renaming" func, as loud, for the duration of the call. 
            -->Previous the function said: "text = func("Hello")
                Now the function is saying:"text = loud("Hello")
                    -->We are now sending the string of text "Hello" to the "loud" function
                            -->"HELLO" is put into upper case by the loud function, and sent back to the hello function.
                                    ---> The resulting "HELLO" is now assigned to the text variable
                                            --->Lastly, we print "text", which is now "HELLO"
    
'''

#Example of higher order function 2.
#HIgher order function returns a function.

'''
Lets say we a pair of nested functions.
'''

def divisor(x):         #Primary function is defined as divisor, and accepts a number called x
    def dividend(y):    #nested function is defined as divident, and accepts a number called y.
        return y / x    #Return the output of the divident function(y) divided by the divisor function(x)
    return dividend     #now we return the output of the dividend function in the outer function.
                        #So a higher order function, is a function, that returns a function. (say that 10 times)
#Divisor is now effectively a higher order function, because its returning its inner funciton.
#So the divisor function, is going to return the dividend function, which is then assigned to the dividend variable

#Now  we create a variable called divide, which calls the divisor function, with the argument 2.
#So all values will be divided by 2.
divide = divisor(2)
#Then we print, and call the divide variable, and parse the dividend as 10
print(divide(10))

'''
So to take it step by step what just happened:
The program starts at divisor and we parse in 2.
x will now be known as 2. And will stay that way, until the program finish.
    --! For now, we skip the dividend function, as it has not been called yet.
        -->Therefore, we return the dividend as an output, and assign it a variable
            +++ We can now call the dividend function, because the divide variable shares the same memory
                address as the dividend function!+++
                    -->print(divide(10)) now we call the dividend function, and parse in 10. Because divide, and 
                        dividend shares the same memory adress!
                            -->dividend is now called, and defined as 10. divisor is still defined as 2.
                                so we return the output of y / x and printing it to the console window.    
'''