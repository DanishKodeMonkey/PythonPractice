#Walrus OPerator :=

#New to Python 3.8
#Assignment expression, aka walrus operator
#Assigns values to variables as part of a larger expression

'''
In practical terms it means that you can both assign and execute a variable on the same line.
While before we had to first assign the variable, then print the variable.
With the walrus operator, we can do both at the saime time.
'''

#Old seperate assign and execute.
'''
happy = True
print(happy)
'''

#New Walrus operator
print (happy := True)

'''
 more practical use of the walrus operator would be :
'''
#Lets create a small program that consist of a while loop that consistently asks for your favorite foods, and
#adds your answers to a list until you write quit.

#Heres the old method
'''
foods = list()  #Assign a variable called foods, and have it be a list.

while True:                                    #While True, keep repeating:
    food = input("What food do you like?: ")        #assign variable food, to be whatever input the user sends.
        if food == "quit":                              #if user input is quit:
            break                                       #break(end program)
        foods.append(food)                          #append the variable called foods, with the food item that the user input.
'''

#Now lets do the same, but in HALF THE LINES!!

foods = list()  #We still need our list, so define a variable as foods, and make it a list.
while food := input("What food do you like?: ") != "Quit"   #But this time, create a while loop that says the following:
#While a input is entered, assign the value to the food variable and repeat, as long as "quit" is not used.
    foods.append(food)  #append the foods list with the input from food.
