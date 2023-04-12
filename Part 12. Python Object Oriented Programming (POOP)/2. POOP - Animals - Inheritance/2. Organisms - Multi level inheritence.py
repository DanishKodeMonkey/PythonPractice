#Multi-levle inheritence is when a  derived(child) class inherits from another derived(child) class

#Following the same pattern as before, lets add another layer.

class Organism:                                 #We create a class called Organism, that will be the parent class
    alive = True                                #Inside the parent class we place a attribute that will cover all child classes.

class Animal(Organism):                         #This time, the Animal class is a child class, and inherits all attributes and methods from Organism.
    def eat(self):                              #Aside from what has been inherited, Animal also has a method called eat.
        print("This animal is eating, nom!")    #When this eat method is called, we print this animal is eating.
#From here we enter a multi-level inheritance.
class Dog(Animal):                              #This time, we define a class called Dog, which inherits from Animal, which inherits from Organism.
    def bark(self):
        print("This dog is barking, woof!")
#Technically you can just keep adding layers like this.
#If you wish to create another child class on the same level as dog, simply place its argument as Animal as well:
class Cat(Animal):
    def meow(self):
        print("This cat is meowing, nyan!")

#Now to check if it works, we will check various attributes and methods that Dog should contain and has inherited.

dog_1 = Dog()
print(dog_1.alive)      #Refering to the parent class "Organism
dog_1.eat()             #Refering to the parent class "Animal"
dog_1.bark()            #Refering to Dogs OWN Method


