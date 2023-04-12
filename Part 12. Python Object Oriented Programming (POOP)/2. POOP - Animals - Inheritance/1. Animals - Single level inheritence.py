#Classes can inherit something, usually attributes and methods from other classes
#These classes form parent-child relationships
#Where a child receive everything a parent has.

#In this example we will create a parent class called Animals,
    #We will keep both the class and object creation in one program this time to make it easier to read.
#which children classes will inherit all of its attributes and methods.

class Animal:   #First we create the parent class, and call it Animal
    #First, attributes.
    alive = True    #We assign it an attribute of alive, that is True, because, well... its alive?
    #And a couple of methods
    def eat(self):  #Define a method called eat, to the object itself.
        print("This animal is eating, nom!") #What does the method do?

    def sleep(self): #Define a method called sleep to the object itself
        print("This animal is sleeping, zzz.") #What does the method do?

#We now have our Animal class.
#now to make the child classes
#In this case lets create seperate classes for specific types of animals
#To inherit from another class, type the name of the parent class in paranthesis() after the new class name
    #The benefit of inheritance is that we dont have to copy and paste the same attributes and methods
        #in every single class. So if someone wanted a attribute name changed, you wouldnt have to change every.single.one
        #So just have a parent class, that holds all the attributes and methods the child classes has in common,
        #and then add whatever attributes and methods to each child class that only they have.
class Rabbit(Animal):
#The Child class(Rabbit) now contains EVERYTHING its parent class (Animal)
    #Furthermore, we can now define the unique attributes and methods to THIS child class
    def run(self):
        print("This rabbit is running")
#Lets do that for 2 more child classes
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

#now lets create some objects
rabbit_1 = Rabbit()
hawk_1 = Hawk()
fish_1 = Fish()

#Now, when you print one of the child classes, you will find that all the attributes and methods in the parent class is avaible
print("The rabbit is alive?: "+str(rabbit_1.alive))
fish_1.eat()
hawk_1.sleep()

#Lets execute some of the unique methods of the child classes now
print()
rabbit_1.run()
fish_1.swim()
hawk_1.fly()


