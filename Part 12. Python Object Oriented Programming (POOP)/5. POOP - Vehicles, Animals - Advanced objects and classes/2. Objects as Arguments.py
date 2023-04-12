'''
This time around we will try and pass objects as arguments
'''
'''
What we will be doing is creating a class called Car, with one attribute called color that has the value as None
We will then be calling a function that wil laccept an object as an argument, as well as its value
'''
class Car:              #Just a class like any other

    color = None        #A attribute with no value.
'''
Now we will create a function that interacts with the attribute as well as its value
make sure to make this function OUTSIDE the class, as otherwise it will be a method.
of the car class, and we need it to be a function outside of it.
'''
def change_color(vehicle,color): #We define the function with two parameters. car, and color. Remember to use lowercase
    '''
    Now when we pass in a car, we will give it a nickname of car
    we will then use color to assign the car color whatever value color is.
    '''
    vehicle.color = color           #vehicle.color value, is the color argument.

'''Now we will use our function change_color to assign a car object as well as a color'''

car_1 = Car()   #Create car_1 object
car_2 = Car()   #Create car_2 object
car_3 = Car()   #Create car_3 object

change_color(car_1, "Red")  #use change_color function to change car_1 color value to Red
change_color(car_2, "White")#etc
change_color(car_3, "Blue") #etc

print(car_1.color)          #print result
print(car_2.color)
print(car_3.color)

'''
Were not limited to using change_color on car objects, we can use it on all sorts of objects.
All we need is a object name, and a color.
Lets create a similar class called Motorcycle, create 3 motorcycle objects, and change their colors.
'''

class Motorcycle():             #create class called Motorcycle

    color = None                #motorcycle class has attribute color = None

bike_01 = Motorcycle()          #Create bike_01 object using Motorcycle class

change_color(bike_01,"Black")   #Change bike_01 object class value color to Black

print(bike_01.color)            #Print the result!
