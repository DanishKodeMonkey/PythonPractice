import os

#Before starting, import the os module to interact with the operating system
#For the sake of the tutorial, create a file called movetest.exe
#The objective of this is to move a file from the projects folder to the desktop
#In order to start moving files we will need 2 variables, 1 for the source, 1 for the destination.

#Define variable source, as the file movetest.txt(path if not in project)
source = "movetest.txt"
#Define variable destination, as path to new folder on desktop(since not in project)
destination = "C:\\Users\\Humbe\\Desktop\\Pythontestfolder\\movetest.txt"

#Remember good practise of writing code that has a potential to fail in a try and except block, to handle potential exceptions.

try:                                            #Try all the code below
    #First some basic file detection!
    if os.path.exists(destination):             #If there already is a file by the name "movetest.txt" in the destination folder
        print("There is already a file there")  #Then print "There is already a file there
    #If a file is not detected, then proceed with moving/replacing
    else:                                       #If no file is found then:
        os.replace(source,destination)          #replace(move) the file from the source, to the destination
        print(source+" was moved")              #When done, print the variable "source" with string "was moved"

except FileNotFoundError as e:                       #If an exception called FileNotFoundError occours, then:
    print(e)
    print(source+" was not found")              #print variable "source" with string "was not found"