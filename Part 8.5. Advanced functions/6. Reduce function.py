'''
The reduce() function apply a function to a iterable(list)
                    and reduce it to a single cumulative value.
                    it performs the function on the first two elements and repeats the process
                    until 1 value remains
Another way to think of it:
Were recycling elements within and iterable(list) until a single item remains!
Syntax:
reduce(function, iterable)
'''
#For this to work we have to import pythons functools
import functools

#Lets say were playing scramble
#From this we have a list of various kinds of letters.

letters = ["H","E","L","L","O"]
'''
We would like to reduce all of these individual elements until only a single culmulative element.
We will store the culmulative element of all the individual elements inside a variable called word
Again, we can use a lambda function, which, this time, we will type directly into the argument.
Make note of how the parameters end with a blank after a comma, this is to continue the parameters afterwards in the 
reduce function.
'''

word = functools.reduce(lambda x,y,:x+y,letters)
print(word)

#now here is what is happening:

'''
our reduce function applies our function to the first two elements(x,y) of our itterable defined as "letters".
    -->it applies the expression x + y(putting them together)
        -->We have now combined two first two elements, x and y, which are H and E.
            So we have HE
                -->The reduce function now repeat the process by combining the previous result HE with the next element L
                    We now have L
                        --->This keeps going until all the elements have been combined into one HELLO
                
'''

#Another example can be made with numbers, by finding the factorial of a line of numbers 5 through 1
#Since we, with factorials, multiply the next two numbers, we have to change the function object to a *
factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y,:x * y, factorial)
print(result)

# again here is whats happening:

'''
our reduce function applies our function to the first two elements(x,y) of our itterable list defined as "factorial".
    -->it applies the expression x * y(multiplying them together)
        -->We have the multiplied number of x and y, which is 20.
            So we have 20
                -->The reduce function now repeat the process by multiplying the previous result 20 with the next element 3
                    We now have 60
                        --->This keeps going until all the elements have been combined into the final result 120

'''
