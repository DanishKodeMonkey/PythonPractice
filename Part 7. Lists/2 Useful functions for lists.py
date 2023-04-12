#Using the same list from before, lets test some functions for it

food = ["pizza","hamburger","hotdog","spaghetti"]

food[0] = "sushi"

#Functions here
#to use functions add a dot to the variable name
#append adds a item to the end of hte list
food.append("ice cream")
#Remove removes an item from the list
food.remove("hotdog")
#pop will remove the last item in the variable list
food.pop()
#insert will add a value at a given index
#Here we insert cake at index 0
food.insert(0,"cake")
#sort will sort the list alphabetically
food.sort()
#clear will clear a list, removing all the elements of a list
food.clear()

#These are just examples, as always there are more.

for x in food:
    print(x)