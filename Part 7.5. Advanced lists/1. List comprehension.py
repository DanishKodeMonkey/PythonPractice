'''
A list comprehension is a away to create a new list with less syntax
                    it can mimic certain lambda functions, and is easier to read
syntax format:
Example 1.
list = [expression for item in iterable]
list =    [expression              for   item    in   iterable]
  V            V--|----------V      V     V       V     V
example = [itteration * itteration for itterable in range(1,11)]

or
Example 2.
list = [expression for item in iterable if conditional
list    = [Expression for   item   in  iterable if  conditional
 V             V             V           V          V----|-------V
example = [itteration for itterable in listname if itteration >=60]

or
Example 3.
list = [expression (if/else) for item in iterable]
list    = [expression (if/else)      for item in iterable]
  V        V V-----------|-------V       V        V
example = [i if i >=60 else "FAILED" for i in students]
'''

#To illustrate, here is a program that will create a list of all the numbers
#1 through 10 squared.

squares = []                #Create a empty list
for i in range(1,11):       #Create a for loop
    squares.append(i * i)    #define what each loop iteration should do
print(squares)

#We made this code in 3 lines. Lets do the same thing, but in a list comprehension with less syntax

'''Syntax example 1.'''
#list = [expression for item in iterable]
'''
So the list is squares, the expression for the item is "i * i", the item in iterable is "i in range 1-11"
'''
squares = [i * i for i in range(1,11)]
print(squares)
#There, we have now done it in one line of code

'''You can also use a comprehensive list to mimic a lambda function'''
#Here we first try to do it using a filter function.
#So we have a list of students grades here
students = [100,90,80,70,60,50,40,30,0]

#We want a list of the passed_students, this list will filter the students list, for all values equal to or higher than 60.
passed_students = list(filter(lambda x: x >=60, students))
#and print the new list.
print(passed_students)

'''Syntax example 2.'''
#Lets try again using a comprehensible list

passed_students2 = [i for i in students if i >=60]
print(passed_students2)

'''Syntax example 3.'''
#Finally lets say we want to replace all failed grades with the world failed
#We can then use a if/else statement in the list comprehension instead.
#Otherwise completely identical to example 2.
passed_students3 = [i if i >=60 else "FAILED" for i in students]
print(passed_students3)