#Type casting converts one datatype of a value to another data type

#Example 1 - No type casting
x = 1   #int
y = 2.0 #float
z = "3" #str

print("Non-typecasted datatypes")
print(x)
print(y)
print(z)

#Example 2, print typecasting
#In order to convert a specific datatype in print, supercede the variable with the given datatype you wish you convert it to
print("print typecasting, tempoairy change")
print(x)
print(int(y))
print(z)

#Example 3, definition typecasting

print("definition typecasting, permanent change")
y = int(y)
print(y)

#Example 4, keep in mind strings cannot be used for any kind of math, multiplying a string will just output the text several times
print("Example of multiplying a string, resulting in several prints")
print(z*10)
#In order to math z, we first have to turn the string into an integer
#Note how the definition typecast is only permanent below the line it is defined.
print("Converting the string into a integer with definition typecasting allows math to happen!")
z = int(z)
print(z*3)

#Example situation where typcasting is useful.
#Say if you need to print a integer or float variable alongside a string line of text.
#You cannot do that as you cannot print two different datatypes at the same line
#Instead what you have to do, is string cast the integer or float, to print the value in a temporary manner
#By the way, should you forget it will say "TypeError: can only concatenate str(not "int") to str
#concatenate means to "merge" or "combine"
print("Example combination print of integer and string text in-line")
print("A magical value of "+str(y))