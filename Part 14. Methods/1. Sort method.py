#Sort() method is used for lists - Syntax (variablename).sort(key/reverse) arguments are optional.
#sort() functions are used for iterables

#Lets start with the method, in this example we have 5 students, which we would like
#to sort alphabetically
students = ["Squidward","Sandy","Patrick","Spongebog","Mr.Krabs"]

#To use the method, simply call the list, and add the sorting method, with the reversed argument to true, to
#sort the list in reverse alphabetical order.
students.sort(reverse=True)

#Now when you print the list in a loop for instance, it will already be sorted.
for i in students:
    print(i)

#Sort methods only work for lists, should you need something similar for iterables, like tuples.
#You will need the function instead
#This time we use the same list, but in a tuple.
students2 = ("Squidward","Sandy","Patrick","Spongebog","Mr.Krabs")

#sorted_students is a list, which is formed from result of the students2 tuple that has been sorted with the sorted function.
sorted_students = sorted(students2,reverse=True)

for i in sorted_students:
    print(i)

'''
Next we will tackle lists of tuples.
Sometimes data isnt as simple as above.
'''

#In this example we have a list of tuples, housing names, a letter grade, and the student age.

students3 = [("Squidward", "F", 60),
             ("Sandy", "A", 33),
             ("Patrict", "D", 36),
             ("Spongebob","B",20),
             ("Mr.Krabs","C",78)]
'''
This is where the key argument come in
The list of tuples resemble a spreadsheet, each collumn holding a similar value. "Name" "Grade" "Age"
To sort this, we have to divide up the tuples values, starting with and choose how to sort the list.
This is a good time to use a lambda function, as it is single use and throwaway once done.
'''

#define "grade" function object, as a lambda function that takes one argument grades: from grades index 1(2nd index since computers count from 0)
grade = lambda grades:grades[1]
#Now we sort the students tuple list, by the grade key, which is index 1 of each tuple.
#And just to show, we will also add the second argument reversed
students3.sort(key=grade,reverse=True)

#And print the sorted list of tuples
for i in students3:
    print(i)

#if you then wanted to sort the tuple list by age, you could change grade and grades to age/ages, and the index to 2
#age = lambda ages:ages[2]
#students3.sort(key=age,reverse=True)

'''
Should you suddenly be faced with a tuple of tuples, you would have to use the sorted function again
it is very similar however
'''
#Heres the same list, but as a tuple of tuples.
students4 = (("Squidward", "F", 60),
             ("Sandy", "A", 33),
             ("Patrict", "D", 36),
             ("Spongebob","B",20),
             ("Mr.Krabs","C",78))

#in this example we will sort by age
#So rename the function object, parameter, and expression to age, and the called index to 2
age = lambda ages:ages[2]

#Again, to use the function sort methods output, we have to wrap it to a variable

sorted_students2 = sorted(students4,key=age)

for i in sorted_students2:
    print(i)


