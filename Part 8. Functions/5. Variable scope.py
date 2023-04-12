#scope -    The scope of a variable is a region that a variable is recognised
#           A variable is only available from inside the region it is created.
#           A global and locally scoped version of a variable can be created

#Example 1. A local scope

def display_name():
    name = "DKM"        #   A local scope is only available inside this function
    print(name)

#Trying to print the variable called "name" will result in an error "The name "name" is not defined,
# since it only exist inside the function.

#Example 2. A global scope
#A global variable is available both inside and outside functions.

name = "Danish Code Monkey"

#now printing name will print the global variable
print(name)

#and if you call the function with the local scope variable, it will be printed since the function ends in a print
display_name()

#Doing this it shows that its possible to use a global and local version of the same variable name

#Python will execute variable names in order by first trying to execute the LOCAL version of name variable if its available
#if its not it will try to execute the GLOBAL version of the name variable

#Python will always follow the LEGB rule executing a variable with the same name in order from top to bottom.
#   L = local
#   E = Enclosing
#   G = Global
#   B = Built-in

