
#There are 4 different datatypes for variables

#While Integers can only store whole numeric data, floats can store decimal portion data.

#Example 1, simple float value would be
print("Example 1, simple float variable printed")
height = 1.98
print(height)

#Example 2, examine a variables datatype with type function, float, short for floating point number.
print("Example 2, Examined height variable datatype with type function")
print(type(height))

#Example 3. Printing a float with a string literal does not go well..
#Again, shrek code, will not work.
#print("Your height is: "+height)

#Correct way is by typecasting height as a string.
print("Example 4. Printing a float alongside a string with typecasting")
print("Your height is: "+str(height)+" meters")