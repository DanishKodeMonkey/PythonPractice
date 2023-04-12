#Slicing creates a substring by extracting elements from an existing string
#This method can also be applied to other operations, but string will be used here.

#When slicing there are 3 optional arguments to keep in mind regardless of the function used.
#[start:stop:step]
#depending on the where and how we want to slice a string


#the indexing operator
#indexing[]
#We define a variable first with several parts in it
name = "Danish Kode Monkey"

#In order to make a substring of the first part of the name variable.
#we will use the indexing slicing method [] and the optional arguments
#Keep in mind computers always start counting at 0.
#So to get the first part of the name we will ask the code to slice the name up from index position 0 to 6

first_name = name[0:6]
#Shorthand you can also write
#first_name = name[:6]
#and Python will automatically assume you mean to start at 0
middle_name = name[7:11]

#and again for the last name, this time leaving the last index out
#Python will then assume that I mean to have the rest of the string in this substring.
last_name = name[12:]

#lastly step is how much we are increasing our index by the value given
#step is by default 1, meaning it uses every single letter
#setting step to 2 will mean it will only use every 2nd letter etc.

#This will make a wierd name substring with step 2, which will create a substring of every 2nd letter

funky_name = name[0:18:2]
#Shorthand again, as long as you use to collons, and the optional functions empty. Python will assume you mean
#the start and/or end of the index, so:
#funky_name= name[::2] would result in the same

#Another use of step optinal function is to reverse a series of substrings.
#
reversed_name = name[::-1]

#finally, print our now sliced up name.
print(first_name, middle_name, last_name)
print(funky_name)
print(reversed_name)
