#A dictionary is a changeable, unordered collection of unique key:value pairs
#It is fast because they use hashing, that allows us to access a value quickly.

#Forming a dictionary simply requires the use of collons to associate a key with a value.
#Keys and values can be of any datatype, seperate key:values with commas(,)
capitals = {'USA':'Washington DC',
            'India':"New Dehli",
            'China':"Beijing",
            "Russia":"Moscow"}
#Now in order to access a value of a key, you must first access the key.
#Notice the similarily to printing a index value.
print("Print the value Moscow from the Key Russia")
print(capitals["Russia"])

#This way is not nessecarily safe, if a user should print a key, like say, germany, that doesnt exist
#the program will be interrupted.

#A much safer way to access a key is to use the get method
print("")
print("Check the dictionary capitals, and see if Germany has a key, print result.")
print(capitals.get("Germany"))
#It will return with none ,and not interrupt the program

#Some examples of functions and methods to use with key:values are
#Keys, scans dictionary for keys
print("")
print("Search dictionary capitals for keys, print keys.")
print(capitals.keys())

#Values, scans dictionary for values
print("")
print("Search the dictionary capitals for values, print values.")
print(capitals.values())

#items, scans dictionary for keys and values
print("")
print("Search the dictionary capitals for keys and values, print keys and values.")
print(capitals.items())

#And again, to list items in a point list. Use a for loop.

print("")
print("For each key and value in capitals dictionary, print they key and value, then itterate next.")

for key,value in capitals.items():
    print(key, value)

#Dictionaries are mutable, so you can edit them as the program is running with functions and methods
#update adds a key:value
capitals.update({"Germany":"Berlin"})

#Update can also change an existing value in an existing key.
capitals.update({"USA":"Las Vegas"})

#Pop removes a key:value pair
capitals.pop("China")

#Clear will remove everything, commented for destructive tendensies
#capitals.clear()
print("")
print("For each key and value in capitals dictionary, print the key and value, then itterate next.")
print("With edited dictionary")
print("")
for key,value in capitals.items():
    print(key, value)