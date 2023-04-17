
'''
Lambda functions are functions that are written in 1 line using lambda keywords
    Lambda functions accept any number of arguments, but only one expression
    Think of it as a shortcut
    it is useful if needed for a short period of time, a throw-away function
'''
#lambda parameters:expression

#As an example, here is a typical double function.
def double(x):          #Define a function called double, with one parameter
    return x * 2        #When double iscalled, take the argument and multiply by 2

print(double(5))        #Print the double function, when argument 5 is input to parameter x.
#5x2=10
'''
#now to do the same thing as a lambda function
#Call lambda function, first x is the parameter, dividing parameters and expressions is done with collon(:)
#afterwards we type the expression x * 2 - "We would like to return x * 2"
#The lambda will return a function object, which can be assigned like a variable
'''

double2 = lambda x:x * 2

#And to check that it works:
print(double2(5))

'''
The syntax is effectively:
lambda (parameters):(function expression)
'''

'''
lets try again with two parameters.
#In this example we have 2 numbers we want to multiply each other by.
'''
#To do this, we add another parameter between lambda and collon(:), followed by the expression that says to multiply the two.
multiply = lambda x, y: x * y
print(multiply(5, 2))

#Again, this time with add, and 3 parameters

add = lambda x, y, z: x + y + z
print(add(5,6,7))

#And again, same concept, but with strings.
full_name = lambda first_name, middle_name, last_name: first_name+" "+middle_name+" "+last_name
print(full_name("Danish", "Kode", "Monkey"))


'''
Lets do something a bit more advanced
say that we want to check somebodys age once to see if they are 18 or older.
'''
#Name of variable equals lambda function, with one parameter called age.
#And function expreesion "Is True if age is bigger than or equal to 18, otherwise False
age_check = lambda age:True if age >= 18 else False
print(age_check(12))