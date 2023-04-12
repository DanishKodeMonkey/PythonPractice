#Multiple inheritence is a child class that derives from more than one parent class.

#As an example we will create 2 types of animals, that we want all animals to fall into one, other, or both.
#We will therefore create 2 parent classes
class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):                 #Rabbit is prey, it flees
    pass

class Hawk(Predator):               #Hawk is predator, it hunts.
    pass

class Fish(Prey, Predator):         #Fish can be both prey and predator, so it can flee and hunt.
    pass

#Now lets test by creating one object for each sub class and see what they do
rabbit_1 = Rabbit()
hawk_1 = Hawk()
fish_1 = Fish()

#Now rabbit_1 only has access to the flee method
rabbit_1.flee()
#Hawk only has access to the hunt method
hawk_1.hunt()
#However fish has access to both.
fish_1.flee()
fish_1.hunt()