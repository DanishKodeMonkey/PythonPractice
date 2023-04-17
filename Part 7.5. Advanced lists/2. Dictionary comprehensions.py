'''
Dictionary comprehension creates dictionaries using an expression
                         it can replace for loops and certain lambda functions

Syntax 1:
(basic)
dictionary = {key: expression for (key,value) in iterable}

Syntax 2:
(conditional)
dictionary = {key: expression for (key,value) in iterable if conditional}

Syntax 3:
(if/else)
dictionary = {key: (if/else) for (key,value) in iterable}

Syntax 4:
Function call
dictionary = {key: function(value) for (key,value) in iterable}
'''

#--------------------------------------------------------------------------------------------------------------------------

'''Syntax 1 Example'''
'''Basic'''
#Here is a list over cities in Fahrenheit
#The list lines up key and values as: city:temprature value in fahrenheit
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicaco': 50}

print(cities_in_F)
#We will be creating a seperate dictionary where all the tempratures will be in celcius instead of farenheit
#using a dictionary comprehension

            #Formula for Fahrenheit->Celcius found on net
            #                       V
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
#Translation:   ^   ^---------------------^           ^_________________________|^___________V
#Dictionary =  Key is      expression       for key(city), and value(temprature) in dictionary cities_in_F using items method.

print(cities_in_C)


#-------------------------------------------------------------------------------------------------------------------------------------

'''Syntax 2 Example'''
'''Conditional'''

#Lets say we have a description of weather instead this time

weather = {'New York': "Snowing", 'Boston': "Sunny", 'Los Angelles': "Sunny", 'Chicaco': "Cloudy"}

#We want a dictionary that only holds the cities that are sunny.
#So we can write this:

sunny_weather = {key: value for (key,value) in weather.items() if value == "Sunny"}
#Translation:
#new list name = key is value for (key,value) in weather items list if value is Sunny.
#So we tell it to check each value in the key:values in weather.items() if the value is "Sunny"
#if it is sunny, put in dictionary sunny_weather
print(sunny_weather)


#------------------------------------------------------------------------------------------------------------------------

'''Syntax 3 example'''
'''(if/else)'''
#Lets copy the example from example 1, with the cities, and this time just write if the weather is cold or hot

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicaco': 50}

#Then copy syntax 3 down and start filling it out:
desc_cities = {key: ("Warm" if value >= 40 else "Cold") for (key,value) in cities.items()}
#Translation:           ^----------------------------^          ^               ^
#dictionary = {key:         (if/else)                   for (key,value) in iterable}
print(desc_cities)

#------------------------------------------------------------------------------------------------------------------------

'''Syntax 4 example'''
'''Function calls'''
#Should a function inside a dictionary comprehension become rather complex, you can also call a function instead.
#Again, copy the dictionary from the first example

cities2 = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicaco': 50}

#And the if/else comprehension above. But with the if/else statement put into a function this time.
#and the function call set in the comprehension list.
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

desc_cities2 = {key: check_temp(value) for (key,value) in cities2.items()}
#So this time the value from key,value from cities2 list is sent to the function, and the output(return) is sent
#back to the comprehension dictionary and input as the value of the key

print(desc_cities2)
