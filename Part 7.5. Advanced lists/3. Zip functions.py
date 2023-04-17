'''
Zip(*iterables) = aggregate elements from two or more iterables(list, tuples, sets, etc.)
                  Creates a zip object with paired elements stored in tuples for each element.
'''

#Lets have an example:
#Say we have two different types of iterables.

#A dictionary for the usernames
usernames = ["Danish", "Kode", "Monkey"]
#And a tuple for our very secure passwords.
passwords = ("p@ssword", "abc123", "guest")

#We want to zip together each value in the two iterables so they are matched together in pairs.
#and each pair is gonna be stored in a tuple as a zip object.

#So we create a new list called users, and inside users we want the zip tuple object, that consist of a username
#and password each.
users = zip(usernames, passwords)

for i in users:
    print(i)
#To clarify, the new list is indeed a zip object.
print(type(users))

print("-----------------")#empty space
#You can form the zip back into a list using a cast.
#Same exact thing again, but with list added to the zip function

users2 = list(zip(usernames, passwords))

for i in users2:
    print(i)
#To clarify, the new list is indeed a zip object.
print(type(users2))

print("-----------------")#empty space
#And since we have only two values, we can also form it into a dictionary using a cast..
#Same exact thing again, but with list added to the zip function

users3 = dict(zip(usernames, passwords))
#But to print a dictionary we ofcouse have to change the for loop a bit
for key,value in users3.items():
    print(key+" : "+value)
#To clarify, the new list is indeed a dictionary object.
print(type(users3))

#You are not limited to 2 iterables however, you can use more.
#For this example, lets make a list of login dates.

login_date = ["1/1/2021","1/2/2021","1/3/2021"]

#Now we create a new zip object with 3 differnt lists to include.
users4 = zip(usernames,passwords,login_date)

#And print each iteration in the new zip list.
for i in users4:
    print(i)