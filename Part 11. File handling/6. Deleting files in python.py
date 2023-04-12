#For this experiment we will need 2 modules
import os           #os to handle files
import shutil       #copyfile() copy() copy2()

#A good practise with file handling is to define them through variables, and use the variables as arguments.
#We will also do some exception handling for practise

path = "deletetest.txt" #Define variable named path as the path to the file called deletetext.txt(with path if not in project)
path2 = "Empty_Folder"
#os.remove does not remove folders however, should a path lead to a folder it will result in a permision error
try:                                    #Exception handling starts here, try code below:
    os.remove(path)                     #os module, remove the file defined in the path variable
except FileNotFoundError:               #If exception "fileNotFoundError" occours then:
    print("that file was not found")    #print "that file was not found"
except PermissionError:
    print("You do not have permission to delete that!")
else:
    print(path+" was deleted")

#To delete folders, use the os modules function called rmdir instead in the same way

try:                                                                        #Again, exception handling!
    os.rmdir(path2)                                                         #os module, remove direction defined in variable path2
except FileNotFoundError:                                                   #catch exception FileNotFound
    print("that file was not found")                                        #print "The file was not found" instead
except PermissionError:                                                     #catch exception PermissionError
    print("You do not have permission to delete that!")                     #print instead
except OSError:                                                             #Catch OSError
    print("The folder contains a file and cannot be removed with rmdir!")   #print instead
else:                                                                       #If no exceptions above happen
    print(path2+" was deleted")                                             #print path2 variable + "was deleted" string
#HOWEVER THIS WILL NOT WORK!
#rmdir ONLY removes folders that are empty!
#Something is hiding in the folder!
#To wipe out the folder, you will have to use the shutil.rmtree function instead.

#!!!HOWEVER BE CAREFUL WITH THIS FUNCTION!!!
#It is considered dangerous as it removes a folder and ALL files contained within!

#shutil.rmtree(path2)    #shutil module, remove tree(folder and all files within defined in path 2 variable


