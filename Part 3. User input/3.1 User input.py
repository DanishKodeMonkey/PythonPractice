#In order to accept input from a user we use the input function

#Lets start by greeting the user
print("Welcome to the input tutorial!")
#"name" is the variable that we assign the user input to. "input" is the function,
#and inside the function we added some text so as to inform th user what we need.
name = input("What is your name?: ")

#We can then perform a print statement that executes immediately after with the new variable
print("Hello "+name)

#Inputs are, by default, ALWAYS of the string datatype, while numbers can be input, it cant be used for math.
#in order to use the user input for math, it must be converted to a integer

#Here we convert a default string input to a integer
age = int(input("How old are you?: "))
#We get sazzy and tell the program age is actually age + 1
age = age + 1
#Then, in order to print it, we have to string cast it back to a string. As we cannot concatenate several datatypes in print
print("Yeah right, your age is actually "+str(age)+" years old, isnt it ;)")

#Lets try again, this time with height as a float so we can use decimals.
height = float(input("How tall are you?: "))

print("You are "+str(height)+"cm tall")