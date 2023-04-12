#Function is a block of code which is executed only when called
#useful for creating a block of code to execute in different places of a program to avoid repeating the same block of code

#Example 1. Basic function
#define new function as unique name hello
def hello():
    #Block of code below
    #Print "hello!"
    print("hello!")
    print("Have a nice day!")

#Call function hello 3 seperate times
hello()
hello()
hello()

#Example 2. Send information to function using parameters and arguments
#You can send a function information too. Again the same block of code,
#this time calling a reference that is unresolved at first.

#define new function with unique name hello2 with the parameter called name
def hello2(name):
    #Block of code below
    #print "hello"+name(unresolved reference)
    print("hello "+name)
    print("Have a nice day!")

#Now call function and write the data in the paranthesis
#This data is called an argument

hello2("Bro")

#What happens is that we call the function hello2, and send a argument over to the function with the string "Bro"
#The function then receives the argument, and nicknames it using the parameter called "name"
#Now the "Bro" argument replaces the "name" parameter and prints "Hello Bro, have a nice day!"

#Example 2. Variables, arguments and parameters
#This is not limited to values, you can send variables too

my_name = "Bruski"

hello2(my_name)

#This will tempoarily give the value "my_name" a nickname of "name"

#You can send more than one value with arguments too

#Define a new function with a unique name hello3, that holds 2 parameters, "first_name" and "last_name"
def hello3(first_name,last_name,age):
    #The block of code executed when the function is called prints "Hello first_name last_name"
    print("helloo "+first_name+" "+last_name)
    #Then we print a message with the integer, casted as a string to avoid conflicts.
    print("You are "+str(age)+" years old")
    print("Have a nice day!")

#We call the function, and send arguments to the parameters in order.
hello3("bro","Code", 21)

#Keep in mind to match the number of arguments and parameters, and keep them in order.