import os

#Before starting to interact with files, its recommended to import the os library, which will let Python interact with
#the operating system to an extend
#For the sake of the test a text file has been created in C:\Users\Humbe\Desktop\DanishKodeMonkey\Python\helloWorld\Part 11. File handling

#To interact with the file we create a variable, and call it path
#If a file path contains backslashes \ you will need to double them \\ since thats the escape sequence in a string
path = "C:\\Users\\Humbe\\Desktop\\DanishKodeMonkey\\Python\\helloWorld\\Part 11. File handling\\test.txt"
#After that we can use if statements to check the path in various ways
if os.path.exists(path):                    #If the os library function path(location) detects the defined path
    print("That location exists!")          #print "That location exists!
    if os.path.isfile(path):                    #If the os library function isfile location sees that the defined path leads to a file
        print("That is a file!")                #print "That is a file!"
    elif os.path.isdir(path):                   #Else If the path is NOT a file, check if the path is a directory
        print("The path is a directory!")       #Print "The path is a directory
else:                                       #If os library function path(location) does NOT exist, defined in variable path
    print("That location doesn't exist!")   #print "That location doesn't exist!

