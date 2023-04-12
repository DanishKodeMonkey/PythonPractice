#Logical operators (and,or,not) are used to chec kif two or more conditional statements are true

temp = int(input("What is the temperature outside?: "))

#Example 1. And can be used to check several conditions of an if, this can be useful for checking a range of value by
#checking if the value is greater than or equal to 0 AND less than or equal to 30 at the same time.
#with an and operator BOTH statements MUST be true in order for the if statement to execute.
if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")
#The or operator can be used to check if EITHER ONE of two conditions are met, if any of the mare met, the code will execute.
elif temp < 0 or temp >30:
    print("The temperature is bad today!")
    print("Stay inside!")
#The not logical operator can check if one or more, conditions and is used to flip a statement to its opposite statement
#Example, doing the same code, but with not, reverses the statements.

    #if not(temp >= 0 and temp <= 30):
        #print("The temperature is good today!")
        #print("Go outside!")

    #elif not(temp < 0 or temp >30):
        #print("The temperature is bad today!")
        #print("Stay inside!")
#Doing this will make it so the if statement will execute if temperature is NOT above or equal to 0 and below or equal to 30.
