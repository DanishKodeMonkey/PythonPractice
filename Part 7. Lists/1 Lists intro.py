#List = are used to store multiple items in a single variable

#to turn a variable into a variable LIST, simply surround it with brackets []
#To illustrate,
#by placing the four different foods in one variable list, and print. It will print all the items in the list
print("Full Variable list of food")
#Here we say
#food is a list of pizza, hamburger, hotdog, and spaghetti
food = ["Pizza","hamburger","hotdog","spaghetti"]
#print the variable list food
print(food)

#to print a specific element of a list, you add the brackets in the print statement
#and determine the index value of the item you want, remember, computers count from 0
#meaning "pizza" is index 0, hamburger, index 1. ETC.

#print food index 0
print(food[0])

#An important value of lists is that you can always update the elements of the list
#Also note, once again, the change happens in order from top to bottom.
#here we now say:"Food index 0 is now sushi
food[0] = "sushi"
#print food index 0 again, now its Sushi
print(food[0])

#In order to list the items in a list neatly one its own lines,
#we just have to use a simple for loop

#For each item in variable list food print each item in order in each itteration
for x in food:
    print(x)

