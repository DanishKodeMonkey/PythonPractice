#There are various functions and methods that can be used for strings.
#Example root, we will use this string for the various examples
#KEEP IN MIND when starting to write something like print(name.find()) a popup appears with all kinds of suggestions to use.
#The ones used here are just examples
name = "Daniel"

#For reference, below is a simple print of the name
print("For this code we will use a simple string variable called Daniel")
print(name)
#Len, or Length is a function that outputs the number of characters in the string
print("Example of Len, or length, a function that outputs the number of characters in a string.")
print(len(name))
#find is used to find a specific letter in a string, and print its location by its number from the left, starting with 0
print("name.find can be used to find a specific letter in the string. The first letter in a string is always 0, counting up")
print(name.find("i"))
#Capitalize defines itself, it capitalizes the first letter in the string.
print("Capitalize... explains itself")
print(name.capitalize())
#Upper makes all string letters capitalized (useful for finding a output from code?)
print("Upper capitalizes the whole string, useful for finding a output maybe")
print(name.upper())
#Lower, same as upper, but lowercase
print("Lower, same as upper, but lowercase")
print(name.lower())
#Isdigit determines if the string has any digits, and outputs as True or False
print("isdigit determines if the string has only digits, and outputs as True or False")
print(name.isdigit())
#Isalpha determines if the string is in alphabetical characters.
print("isalpha determines wether or not the string contains only alphabetical characters and outputs as True/False")
print(name.isalpha())
#Count will count how many of the defined letters are in the string
print("Count will cound the amount of the defined letter is in the string, in this case, the letter i appears once")
print(name.count("i"))
#replace replaces all instances of one letter with another letter in output
print("replace replaces all defined letters in the string with another defined letter, in this example replace a with o")
print(name.replace("a","o"))
#Python is able to print the same output several times simply by using multiplying it.
print("Python is able to output a given variable several times by multiplying it in code")
print(name*10)
