#An if statement is a block of code that will execute if its condition is true

#Example 1 - Age check
#Set up a user input as a integer
age = int(input("How old are you?: "))
#Set up a if statement to check if the user is 18 or above
#Notice the code below the if statement is indented, this is the block of code that will be executed if its true
if age >= 18:
    print("You are an adult!")
#Now if the user inputs any age at or above 18, the if statement will execute the print. If its not, we skip the print.
#It is possible to check more statements by adding more lines between if and else, using the else-if statement
elif age == 100:
    print("You are a century old!")
    #NOTE: In order to check if a value is equal to a value, use double equal signs ==, single equal signs are used for ASSIGNMENTS
elif age < 0:
    print("You havent been born?!")
#In order to make a reaction for when the if statement is false, we then use a else statement.
else:
    print("You are a minor!")
#Now if the if statement is false, the else-if statement will be executed, if that too is false, we will move on to the else statement.
#This will all be done in the order they are written
#Note how if you input age 100 in this program, it will simply execute the if statement of "you are an adult"
#because it is the first in order.
#To remedy this, re-order the input if statements a bit.
    #if age == 100:
        #print("You are a century old!")
    #elif age >= 18:
        #print("You are an adult!")
    #elif age < 0:
        #print("You havent been born?!")
    #else:
        #print("You are a minor!")

#To summarise, if statements start a chain of true or false checks during an input, elif are different stages
#of this chain of true false checks, and else is the final solution if all else is false.