#A set is a collection which is UNORDERED, and UNINDEXED. No duplicate values are allowed.

#Sets are determined much like lists and tuples, but with curlybracket{} instead of brackets[] or paranthesis()
utensils = {"fork", "spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

#Now to print them in point form
print("For each item(x) in set(utensils) print each item.")
for x in utensils:
    print(x)
#A set computes faster than a list, but is unordered ,so each time it is printed or called it does so faster, but
#more unorganised

#A few useful methods and functions used with sets are

#add, adds an item to the set
utensils.add("napkin")
#remove, removes an item from the set.
utensils.remove("fork")
#clear, clears the set, removing all items. (commented for the sake of previous examples)
#utensils.clear()

print("")
print("For each item(x) in set(utensils) print each item. With added methods and functions.")
for x in utensils:
    print(x)

#update merges two sets together
utensils.update(dishes)

print("")
print("For each item(x) in set(utensils) print each item. Update with dishes set")
for x in utensils:
    print(x)

#You can also join together two sets entirely by creating a new set
dinner_table = utensils.union(dishes)

print("")
print("For each item(x) in set(dinner_table) print each item.")
for x in dinner_table:
    print(x)

#Difference compares two sets to find differences there are between two sets.
print("")
print("Print what utensils has, that dishes doesnt")
print(utensils.difference(dishes))

#Intersection finds what two sets has in common
print("")
print("What does utensils and dishes have in common?")
print(utensils.intersection(dishes))
#It doesnt turn out proper due to the update done above.