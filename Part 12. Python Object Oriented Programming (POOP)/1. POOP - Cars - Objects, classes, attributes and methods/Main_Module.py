#An object is an instance of a class,
    #by using programming we can create represantations of real-life objects.
    #This means that we can use programming to mimic real world objects by assigning
    #a combination of attributes (Is/has). Ex. name, age, height.
    #And methods (actions, what an object can do) ex. eat, sleep, make coffee

#To create a OBJECT we first have to create a CLASS
    #A class is a blueprint that describe what attributes and methods that the object will have.
        #You can create classes in the main module, or a seperate module solely for the class(or several classes)
        #Creating classes in the main module is fine for small projects.
        #But for larger projects seperating things into several modules can be useful.

#For this example a seperate module called car can be found. Here we will simply import and use it

#To import a module in the project folder, simply refer to it with the import function
#In this case we import the Car class from the car module

from car import Car

#To create a object, we must create a unique name for it, and refer to the Car class
#To quickly check what arguments is requires, simply pass the Car() with empty arguments and it'll say whats needed in the error console.
car_1 = Car("Ford","Mustang","1990","Black") #Create a object called car_1 using the Car class(formula)

#We can then print this objects values.
print("Car 1 is a "+car_1.make+" "+car_1.model)
print("From the year "+car_1.year)
print("The "+car_1.make+" is "+car_1.color)
print("The "+car_1.make+" has "+str(car_1.wheels)+" wheels.")

#You can then use the Car classes methods with the object.
print()
car_1.drive()
car_1.stop()

print() #Just an empty line

#There is also a type of attribute variable, called a class variable, which sets a default value
#In this case a class value has been set outside the constructor called Wheels.
#We can check the default value of the Wheels attribute by printing it in a call.
print()
print("By default, all cars have "+str(Car.wheels)+" wheels")
print()
#Now the cool part of the objects is that we can create any number of objects using the Car class

car_2 = Car("Chevy","Corvette","2021","red")
#However we would also like to change the class variable wheels (which assigns all objects a wheels values of 4) to 2
#Should we change our mind and want ALL cars to have 2 wheels by default, we can change all instances of the cars amount
#of wheels by defining it here.
#Car.wheels = 2     <- Define Class Car Class Variable wheels as 2.
#after that all car instances would have 2 wheels.
car_2.wheels = 2

#Now print the result.
print("Car 2 is a "+car_2.make+" "+car_2.model)
print("From the year "+car_2.year)
print("The "+car_2.make+" is "+car_2.color)
print("The "+car_2.make+" has "+str(car_2.wheels)+" wheels.")
print()
car_2.drive()
car_2.stop()

#The method calls can also be done independently, useful for executing a object method at any time
print()

car_1.drive()
car_2.stop()
car_1.stop()
