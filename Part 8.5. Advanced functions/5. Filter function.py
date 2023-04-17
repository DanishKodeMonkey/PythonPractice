'''
The filter function creates a collection of elements from an iterable for which the function returns True

Syntax:
filter(function,iterable)
'''

#Lets say we have a list called friends, each tupple holds a friends name and their age.

friends = [("Rachel", 19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

#We would like to create a list, for all the friends who are 18 or older.
#Because we are going out drinking or something
#Lets use a lambda function again, to seperate the age index [1] and make sure that age is above or equal to 18.
age = lambda data:data[1] >= 18

#For reference here is the filter syntax again
#filter(function,iterable)
drinking_buddies = list(filter(age,friends))
#We will also cast the filter functions output as a list to print it in a while loop
#So the above line says the following:
'''
define new variable called "drinking_buddies", which uses filter function with age function object, on friends list
and print the output as a list, and assign that list to drinking_buddies
'''

for i in drinking_buddies:
    print (i)

#And there! Everyone above 18 listed!
#A good way to think of it is as a search result, we search for a specific piece of data, and pull it from the list.
#and put it into a new list.