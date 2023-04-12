#In order to use various number based functions we import the math module

import math

#Now we use pi, or atleast the first couple decimals of pi, and play around with it
print("Simple definition and print of pi for reference")
pi = 3.14
print(pi)

#Round, is a built in python function, rounds the number to the nearest whole integer.
print("Round")
print(round(pi))

#ceil(ceiling) is a math function from the math module, in order to use it we have to refer to the math module in-line
#ceil rounds a number UP to the next full integer value
print("ceil(ceiling)")
print(math.ceil(pi))

#floor, same story, refer to the math module
#floot, rounds the variable DOWN to the nearest whole integer value
print("floor")
print(math.floor(pi))

#Absolute, or abs for short outputs the absolute value of a number
#It will tell you how far a value is from absolute 0
print("Absolute(abs)")
print(abs(pi))

#pow will raise a base number to a power defined.
print("pow(power)")
print(pow(pi, 2))

#Sqrt(squareroot) is a math module
#As the name suggest it finds the square root of a number
print("Sqrt(squareroot)")
print(math.sqrt(pi))

#Max will find the highest value amongst any number of variables.
#Notice how the math module is not called because Max is built into python
#For this example we will create various random variable values

x = 1
y = 2
z = 3

print("Max")
print(max(pi,x,y,z))

#Min function finds the lowest of said values

print("Min")
print(min(pi,x,y,z))