# a while loop is a statement that will execute its block of code as long as a condition remains true, imagine a on and off switch.
#Keep in mind that using a while loop its recommended to create some way to end the loop or you will form a infinite loop.

#Example of an infinite loop
#while 1==1:
#    print("Help! I'm stuck in a loop!")

#An example use of a while loop can be to consistently ask for a name if a user attempts to skip it.

#First we create a variable called name, that is blank so the user can fill it.
name = ""
#Now we check if the length of the name variable is 0
while len(name) == 0:
#While the length of the name inputted is 0, we will ask to input a name again, and again.
    name = input("Enter your name: ")
#Finally, should the length of the name be higher thank 0, it will end the loop by printing hello name
print("Hello "+name)

#There are always different approaches to the same result, and one is not nessecarily better than the other.
#For example, by defining name as none, and forming a loop with not, the intend will be reverse.
#Achieving the same result.

name = None

while not name:
    name = input("Enter your name: ")
print("Hello "+name)