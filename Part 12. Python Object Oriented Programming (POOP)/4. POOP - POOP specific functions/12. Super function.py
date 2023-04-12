
'''
The super function is used to get access to the methods of a parent class.
It returns a temporary object of a parent class when used
'''

'''
In programming, we prefer to reuse code over repeating it. In this example if you create the program below
it is clear that certain variables are called multiple times.
This can be done better by placing any attributes in the Rectacle parent class rather than the child
sub class.
'''
#Wrong, were repeating code!
# class Rectangle
#     pass
#
# class Square(Rectangle):
#
#     def __init__(self,length,width):
#         self.length = length              <--- Defined twice
#         self.width = width                <--- Defined twice
#
# class Cube(Rectangle):
#
#     def __init__(self, length,width,height):
#         self.length = length              <-- Defined twice
#         self.width = width                <-- Defined twice
#         self.height = height
#
# square_01 = Square(3, 3)
# cube_01 = Cube(3, 3, 3)

#Much better!
'''
now in order to use the innit functions attributes from the Rectangle parent class we will 
use the super function!
'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self,length,width):
        super().__init__(length,width)          #Moved self. length and width up, and using super to call it from parent
    #To test this, we can use an area method.
    def area(self):
        return self.length*self.width
class Cube(Rectangle):

    def __init__(self, length,width,height):
        super().__init__(length,width)          #Moved self. length and width up, and using super to call it from parent
        self.height = height                    #Still have to define the height tho, as it only occurs here.
    #To test this, we can use a volume method.
    def volume(self):
        return self.length*self.width*self.height

square_01 = Square(3, 3)
cube_01 = Cube(3, 3, 3)

#Then to finish the test, we call the two methods.
print(square_01.area())
print(cube_01.volume())

#Boom! It works! Were succesfully calling the __init_ function in the parent class, and creating and calling methods on each sub class.