#2d lists are effectively lists of lists

#To illustrate we make 3 lists
#variable list drinks contain coffee, soda, and tea
drinks = ["coffee","soda","tea"]
#variable list dinner contains pizza, hamburger and hotdog
dinner = ["Pizza","hamburger","hotdog"]
#variable list desser contains cake, and icecream.
dessert = ["cake","icecream"]

#Now we combined the 3 lists into 1 variable called food
#food is a 2d list of variable lists drinks, dinner, and desert.
food = [drinks, dinner, dessert]

#and print food, making all 3 lists line up in print.
#Print 2d list food
print("Print 2d list food")
print(food)

#to print just a single list, just like with a single list. Add brackets with the index number of the list
#Print list index 0(drinks), from 2d list food
print("Print list index 0(drinks), from 2d list food")
print(food[0])

#Furthermore, add another bracketed index for the item in that list to print that single item
#print list index 0(drinks), item index 1(soda), from 2d list food.
print("print list index 0(drinks), item index 1(soda), from 2d list food.")
print(food[0][1])
