import shutil
#Importing the shutil module will grant 3 basic functions.
#copyfile() =   Copies contents of a file
#copy()     =   copyfile() + permission mode + destination can be a directory
#copy2()    =   copy()  + copies metadata(file's creation and modification times)

#To access the copyfile function, refer to the module, then the function. (module.function())
#copyfile has 2 arguments. src(source), and dst(destination)

shutil.copyfile('test.txt','copy.txt')   #Shutil module, copy the file called text.txt(path if not in project) to copy.txt(path if not in project)

#The arguments are exactly the same for copy() and copy2()
