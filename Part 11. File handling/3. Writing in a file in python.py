#In order to write in a file, use the same approach as when reading.
#By default the open function of the with statement uses a second argument called 'r' for read.
#If you want to write instead, use the second argument 'w' for write.

#To start, we make a variable with a string of text.
#to add a new line use \n for new line
text = "The text has been succesfully written!\nThis has been a good time\n"

with open('writetest.txt','w') as file:      #With the file called writetest.txt, open and write, and assign as variable file., close when done.
    file.write(text)                    #write the contents of the text variable, in the file variable(which has been opened)

#Now by executing this, a new file will be created, if it does not already exist,
#with the string from the text variable.
#If the file name already exist, it will be overwritten

#If you want to add something to a file without overwriting the existing contents, use the append argument instead.
#A new variable is defined called text 2
text2 = "Have a pleasant day!"

with open('writetest.txt','a') as file: #With the file called writetest.txt, open and append, and assign as variable file.. close when done.
    file.write(text2)                   #Write(append) the contents of text2 in file.
