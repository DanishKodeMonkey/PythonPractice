#Keyword arguments are arguments preceded by an identifier when we pass them to a function.
#The order of the arguments doesnt matter, unlike positional arguments.
#Python knows the names of the arguments that our function receives.

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

#To use keyword arguments simply precede the arguments with the desired parameter. Matching them together.

#They keyword arguments in this case are the red letters, last middle and first.
#By doing this, when we call the function, the function will know which arguments match with which parameter.
hello(last="Runge",middle="Ljung",first="Daniel")