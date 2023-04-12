'''
An abstract class prevents a user from creating an object with that class
It also compels the user to override the abstract methods in a child class

An abstract class = a class which contains one or more abstract methods
An abstract Method = a method that has a declaration but does not have an implementation

A way to see a abstract class is as an template, and idea. That is not real
Its a "ghost" class.
'''

'''
To create an abstract class we will need some imports.
From abc - Abstract Based Class
we import ABC and abstractmethod
'''
from abc import ABC, abstractmethod

'''Then, to make this class an abstract, add ABC as arguments to the class name.'''
class Vehicle(ABC):                             #Activate the Abstract function in this class
    '''And add @abstractmethod to the method.'''
    @abstractmethod                             #Activate the abstractmethod function in this method.
    def go(self):                   #Parent class Vehicle has a go method
        pass                        #The go method is only defined however, with a pass in its implementation.
    @abstractmethod                             #Activate teh abstract method function in this method
    def stop(self):                 #Parent class vehicle has a stop method
        pass                        #But it has no implementation.
'''
This class is now an abstract.
in order for this to work, a abstract class requires atleast ONE abstract method.
'''
'''
A way to look at this is as the Vehicle parent class telling its Car and Motorcycle child classes
"If you are going to inherit from me, you will need to override my go method with your own!"
'''
'''
And since all abstract methods MUST be implemented in its own way in each child class
it is very accurate to think of this as a blueprint, as the program wont work
unless all the parent abstract classes are implemented and overriden by each
child sub class
'''
class Car(Vehicle):
    def go(self):                   #In Car, we override this method by creating a method of the same name
        print("You drive the car")  #With a implementation
    def stop(self):                 #And since BOTH abstract parent methods MUST be implemented and overriden
        print("You stop the car")   #We implement the stop method here as well

class Motorcycle(Vehicle):

    def go(self):                       #Motorcycle also overrides Vehicle by creating its own method
        print("You ride the motorcycle")#With an implementation.
    def stop(self):                     #And since BOTH abstract parent methods MUST be implemented and overriden
        print("You stop the motorcycle")#We implement the stop method here as well

'''Below we create an object for each class.'''
#vehicle_01 = Vehicle() <-- An object cannot be created for a abstract class.
car_01 = Car()
motorcycle_01 = Motorcycle()

'''And execute their methods.'''
# vehicle_01.go()   <-- A object method cannot be executed for a abstract object since it cannot be created from an abstract class.
car_01.go()             #This class will print its method
motorcycle_01.go()      #This class will print its method
car_01.stop()           #This class will print this method
motorcycle_01.stop()    #This class will print this method



