'''
The map function applies a function to each item in a iterable(list, tuples, etc.)

syntax:
map(function,iterable)
'''

#In this example we have an online store.
#This stores items is housed in a list
#Each item and their price are in a tuple, in said list.

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]
'''
Lets say that we want to convert the value of each item, current set in dollars, to euros.
For this example we say the exhange rate for euros are 1 dollar for every 0.82 euro.
This conversion can be done easily with a throw-away lambda function
'''

#to_euros is defined as a lambda function with parameter name data, which
#then grabs a tuple represented by paranthesis(),
#and the data from index 0(item name eg. shirt), but do nothing.
#And data index 1(item price eg. 20.00), and multiplies the value by the exchange rate.
to_euros = lambda data: (data[0],data[1]*0.82)
#The first column 1 is untouched, by column 2 is multiplied by 0.82

#Now the map function is going to create a map object, which can easily be cast to another iterable.
#So we now create a new list called store_euros
        #The map function will execute the function called to_euros, to all valid data inside the "store" list.
            #we cast the function in a list, and set the output as store_euros.
store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)

#lets say the values in the store list, were in euros (eg. 20 euros for shirt(damn, expensive)
#We can convert this to dollars by the same process, but divice by 0.82 since the dollar is worth more than the euro.

to_dollars = lambda data: (data[0],data[1]/0.82)

store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    print(i)