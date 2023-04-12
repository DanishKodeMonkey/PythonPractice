#A tuple is a collection which is ordered and unchangeable
#they are used to group together related data

#The process of creating a tuple is very similar to lists, but instead of brackets[] we paranthesis()
student = ("Daniel",29,"male")

#A tuple can be inspected in various ways, count will count how many times a given item appears in a tuple.
print("Count the number of times the value Daniel appears in the tuple")
print(student.count("Daniel"))
#Checking the index of a item will print its location index in the tuple.
print("Print the index location of the value male in the tuple")
print(student.index("male"))

#A few tricks you can do with a tuple is that you can
#You can display all of the contents in a tuple with a for loop

#Print all values in student once
print("Print all the values in the student tuple once.")
for x in student:
    print(x)

#You can also use if to search for a certain value in a tuple
print("If value Daniel appears in tuple student, print Daniel is here!")

if "Daniel" in student:
    print("Daniel is here!")