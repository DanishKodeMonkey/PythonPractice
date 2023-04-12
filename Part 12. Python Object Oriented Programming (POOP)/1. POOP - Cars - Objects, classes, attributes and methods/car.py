#To create a class we define it similarly as a function is defined.
#For reference here is what a class includes again:
#A class is a a combination of
#   attributes (Is/has). Ex. name, age, height.
#   And methods (actions, what an object can do) ex. eat, sleep, make coffee

class Car:      #Define a class named Car
    #Now to add some attributes and methods to the class.
    #Keeping in the same mindset as before:
    #An attribute define what a class is, and has. So what does a car have, and what is it?

    #First we will put some attributes in a Class Variable
        #A class variable is declared inside a class, but outside a constructor.
        #These can be used to set some default values to some attribute variables.
    wheels = 4  #This is a class variable, which sets all cars wheels to, by default, be of the value 4.
                #This CAN be changed however when the object is created in the main module(see example there)

    #Now we will place some attributes inside a SPECIAL METHOD called the __init__ method
        #The __init__ method, short for initialise, is a special method that will construct objects for us.
        #Other programming languages call this the constructor.
        #ALl variables inside the __init__ method can then be assigned unique variables.
        #And all variables inside the __init__ method are called INSTANCED variables, as they only exist
        #inside the constructor
    def __init__(self,make,model,year,color): #So here we define the initialiser, with the argument self.
                        # The argument refers to what object drive applies to, in this case, its the object self.
                        #We can now receive argument.
                        #But we need to set up some parameters to do so.
                        #In this case we will set the parameters to make, model, year, and color. See below.
        #Now to receive the arguments through the parameters, we must refer to the object were creating.
                        #All variables formed inside the __init__ definition are called INSTANCED variables
                        #as they only exist INSIDE the constructor
        #SO! what is a car, what can it have?
        #It can have a make, so define a variable called make
        self.make = make       #self(the object).make = whatever the argument make is set to in the parameter
        #It can have a model
        self.model = model     #self(the object).model = whatever the argument model is set to in the parameter
        #It can be from a specific year
        self.year = year       #self(the object).year = whatever the argument year is set to in the parameter
        #And hell, it can have a color
        self.color = color     #self(the object).color = whatever the argument color is set to in the parameter

    #Now as to Methods, what can a car do?
    #These are defined as functions(As the name suggest, the function of a car)
    def drive(self):    #define a method function called drive, which applies to the object iself.
        #Now what do we want to do when we call this argument?
        print("This "+self.model+" is driving") #We will print some text, and refer to an attribute of the object(self)
                                                    #the "self" in the object will automatically be replaced by the objects name
                                                    #after the object has been created. so if we call self.model of the object car_1
                                                    #it will automatically adjust to car_1.model or whatever object we refer to.
                                                    #self in this case is simply a placeholder for the objects name.
    #Lets create a stop method as well
    def stop(self):     #define a method function called stop, which applies to the object itself
        print("This "+self.model+" has stopped")

#Now that we have both a constructor, with attributes, and methods defined, we can import the class in another module.
# And start making some cars!