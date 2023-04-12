#Method overriding is the act of overriding a already defined method in a parent class.

class Animal:
    def eat(self):
        print("This animal is eating")
#To override the method eat we will need to define the same method signature in the child class
    #A method signature is the name and parameter of a method. In this case, "eat(self):" is the method signature
class Rabbit(Animal):
    def eat(self):
        print("This Rabbit is eating carrots")

#Now when calling the rabbit_1 object, it will instead write what the child class has printed rather than its parent class.
rabbit_1 = Rabbit()
rabbit_1.eat()