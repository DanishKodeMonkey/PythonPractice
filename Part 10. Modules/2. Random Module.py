import random #importing a module usually happens at the start of the program

#Using the random features in a program will never create a truly random result, computers
#will only ever generate psuedo-random numbers which are fairly close.

#After importing the random module we have access to everything inside
#To use the random module, simply refer to it and its sub-module.

x = random.randint(1,6) #Define a variable that is determined by the random module, to find a random integer between 1 and 6

print(x)    #Then, when printing x, the module will generate a pseudo-random number every time

#The same goes for floating point numbers

y = random.random() #Define a variable y, that is determined by the random module, to find a random number between 0 and 1

print(y) #Now when printing y, we will get a random floating point number between 0 and 1.

#A more practical use of randoms could be done by making a simple game of rock-paper-scissors

myList = ['rock','paper','scissor'] #First we create a list with 3 values, rock paper and scissor
z = random.choice(myList)           #Then we create a new variable z, that will be determined by the random module, using a choice in myList
print(z)                            #And print to see if we lose!

#Another sub-module is shuffle that mixes the different values in a list.
#Example -  The deck of cards

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"] #First we create a list of the different values of a single suit of cards
random.shuffle(cards)                       #Then we simply tell the random module to shuffle the cards list
print(cards)                                #and print the result