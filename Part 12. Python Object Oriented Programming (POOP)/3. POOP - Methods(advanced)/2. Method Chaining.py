#Method chaining is used to call multiple methods sequentially
#                       Each call  performs an action on the same object and returns self.

#For this example we bring the car back, this time the car class has 4 methods, turn on, drive, brake and turn off
#all of which print a simple message
#However in order for method chaining to work we need to return each method to self
#If nothing is defined Python will default to None
class Car:                                     #Create a class called Car
    def turn_on(self):                         #Define a method called turn_on that applies to self
        print("You start the engine")               #When called, it will write a message
        return self                                 #Afterwards, it will return to self(the object)
    def drive(self):                           #Define a method called drive that applies to self(object)
        print("You drive the car")                  #when called it will write a message
        return self                                 #afterwards it will return to self(object)
    def brake(self):                                #etc.
        print("You step on the brakes")
        return self
    def turn_off(self):                             #etc.
        print("You turn off the engine")
        return self

#now we will create a car object
car_1 = Car()

#Now to perform Method chaining, we will call several methods immediately after each other in order.
#You can pick and choose whichever method you need in whichever order you like.
#Should you end up doing alot of method chaining, it is recommended to bring each method call down one line with enter.
#The slash will automatically be inserted, which indicates a line continuation
car_1.turn_on()\
    .drive()\
    .brake()\
    .turn_off()