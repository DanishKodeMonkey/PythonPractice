#An index operator[] gives access to a sequences element including, but not limited to (str, list, tuples)

#First we create a variable
name = "kode Monkey!"

#Here we check if the first letter is capitalised, if it isnt, then we capitalize it.
#if element 0(first letter) of variable name islower(is lower case), then capitalize
if(name[0].islower()):
    name = name.capitalize()
print("")
print("Print variable name after capitalizing in code")
print(name)

#Here we create a substring by naming a new variable, and defining it as the first 4 letters of the name variable
#and then putting it all in upper case
first_name = name[:4].upper()
#Same idea here, we print the last name by creating a substring variable and extracting
#index value 5-end from name, then putting it all in lowercase
last_name = name[5:].lower()
#You can also pull the last character from the variable by using negative indexing, effecting counting backwards.
last_character = name[-1]
print("")
print("Print new substring first_name cut from variable name, then set all uppercase")
print(first_name)

print("")
print("Print new substring last_name cut from variable name, then set to lowercase")
print(last_name)
print(last_character)
