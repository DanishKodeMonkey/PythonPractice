#A str.format() =   a optional method that gives users
#                   more control when displaying output

#Using previous processes we would usually form a string and variables as so:
#animal = "cow"  #Form a variable holding the string "cow"
#item = "moon"   #Form a variable holding the string "moon"

#print("The "+animal+" jumped over the "+item)

#This will naturally print "The cow jumped over the moon"

#But there is a more elegang method of approaching this, using string format fields

animal = "cow"      #Form a variable holding the string "cow"
item = "moon"       #Form a variable holding the string "Moon"
    #Print the sentence, but use {} as placeholders for the format fields, and end the string with.format and its parameters.
    #The parameters can be both strings, or variables, and will input those parameters in order of the format fields
#print("The {} jumped over the {}".format(animal,item)) #Print "The {format field 1} jumped over the {format field 2}
    #The same thing can be done with positional arguments
#print("The{0} jumped over the {1}".format(item,moon)) #Print "The [format field index value 0] jumped over the [format field index value 1]
    #This can also be done using keyword argument pairs
#print("the {animal} jumped over the {moon}".format(animal="cow",item="moon"))
    #A even more elegant way to format this is by storing the string we want to format inside a variable
text ="the {} jumped over the {}" #Define a variable with the string "the {format field 1} jumped over the {format field 2}
print(text.format(animal,item)) #Print the text variable, but format it by inserting the animal and item variables in order

    #This approach can be used to add padding to a string.
        #First, form a variable called name with a string
name = "DKM"
        #then, like before, format a {format field} with the variable
        #To add padding to the format field, before or after, make a collon, and a value of how much padding you want
        #on either side of the variable, determening the direction with <,^,>
print("Hello, my name is {:>10}".format(name))

        #To add a positional argument or keyword argument to the format field, precede the : with the index or key
        #   e.g. {[1]:>10} or {russia:>10}

    #Lastly, to format numbers we have a few methods oto

        #By adding .2f to the format field we effectively tell python to only use the first 2 digits(or whichever number digits we want)
        #Keep in mind it will round up the digits
number = 3.14159
print("The number of pi is {:.2f}".format(number))

        #You can also a comma on each 1000th place of a number with a comma(,)
number2 = 1000
print("The number is {:,}".format(number2))

        #A cool thing is that you can create a binary representation of the number with b(binary)
print("The binary number is {:b}".format(number2))
print("The binary number is {:o}".format(number2)) #Same with octals
print("The binary number is {:x}".format(number2)) #And hexidecimals(x lowercase or X uppercase
print("The binary number is {:E}".format(number2)) #and scientific notation(e lowercase or E uppercase
