#In order to open and read the contents of a file, and print them, we first have to access the file.
#To access a file, you can use the with statement, which access a file easily

#As long as the file is in the projects folder you can refer to the file from the root of the project folder.
#If the file is located out side the project folder you will need the full file path to find where it is.

#In extension, lets practise our exception handling while were at it.
#By wrapping all the code in a try and accept block

try:                                    #Try the code below
    with open('test.txt') as file:      #With the file test.txt, open it, and define this as a variable called file.
        print(file.read())              #with the opened variable called file, read the contents and print them.
except FileNotFoundError:               #If the code results in a filenotfound error then:
    print("The file was not found :(")  #print "The file was not found :("

#Should a typo have happened somwhere and the file is not found, the program will not be interrupted,
#But will print a error statement, this is good common practise to try and get ahead and debug as you go.

#The With statement will automatically close the file after using it.
#To confirm this, you can print wether or not the file has been closed
#Print wether the variable called file is closed.
print(file.closed)