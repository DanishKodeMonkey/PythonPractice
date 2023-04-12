'''
Duck typing is a concept where the class of an object is less important than the methods/attributes
that the class might have
the class type is not checked if the minimum methods/attributes are present
"If it walks like a duck, quacks like a duck, then it must be a duck" -Popular phrase
'''

#Example
'''In this example, the Duck class, and the chicken class have both walk and talk methods, but with different prints'''
class Duck:
    def walk(self):
        print("The duck is walking")

    def talk(self):
        print("This duck is qwuacking")    #<---- Notice the difference

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")   #<--- Notice difference


'''now lets say we have a third class'''
'''The purpose of this class is to catch a duck'''

class Person:
    '''In this case we will pass in self, as well as a duck object as an argument.'''
    def catch(self, duck):
        duck.walk()                #We will use the duck walk method
        duck.talk()                #We will use the duck talk method
        print("You caught the critter!")    #And print "you caught the critter!"

'''Now we create a object for each class.'''
duck_01 = Duck()
chicken_01 = Chicken()
person_01 = Person()

'''To use the catch method, we need to pass in the duck as an argument since its a required parameter in the method'''

person_01.catch(duck_01)
print() #Just an empty line to seperate

'''You can use this catch method with any object however, as long as it has matching methods. Like the chicken!'''
person_01.catch(chicken_01)

'''
Think of it like this:
Python is examening the chicken object, its using its walk method, its using its talk method which is required.
And as a result Python goes:"WELP thats close enough, thats a duck object!
'''