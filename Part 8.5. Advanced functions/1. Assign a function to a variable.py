#Functions can be assigned to a variable.

'''
As we know, defining a simple print function is quick.
'''

def hello():            #Define a function called hello
    print("Hello!")     #When function is called, print hello

hello()                 #call function hello

#An interesting sidenote
#When you PRINT a function, without paranthesis ()
# python will tell you where the function is located
#on the computers memory. something like 0x0225D850

print(hello)        #this will print the current location of the function in memory. It changes every time.

#Furthermore you can assign the assign the adress to a variaable

hi = hello      #So we create a hi variable, and assign it the hello function.

'''
Now if we call either hi, or hello, it will call the function hello. Almost as if the function now has a nickname
and responds to both its actual name, and nickname.
'''

print(hi())     #Call the hi function in a print.
print(hi)       #print the function location in memory.
print(hello())  #call the hello function in a print
print(hello)    #print the function locatiojn in memory.

#Notice how both the variable, and function call the same function AND adress? They are the same!
print()#empty space

'''
Another demonstration:
Lets say we want to assign a built in print function to a variable:
'''

say = print                     #We assign the print function to the variable say.
say("Wow! It works! amazing!")  #now when we call the say variable with a string input it will simply print it!
