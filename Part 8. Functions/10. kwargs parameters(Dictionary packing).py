#**kwargs is a parameter that will pack all arguments into a dictionary
# Useful so that a function can accept a varying amount of keyword arguments

#first we define the function, and pack all arguments into a dictionary with a kwargs parameter
def hello(**kwargs):
    #In order to access the data input into the kwargs parameter we have to use indexing[] for each key
        print("Hello " + kwargs['first'] + " " + kwargs['last'])

hello(first="Danish",middle="Kode",last="Monkey")

#This works, but will still only print the first and last key values.
#To print all key values we have to form a itteration for each input.
#This can be done with a for loop

def hello2(**kwargs2):                  #Define a new function called hello2, and form each argument into a key value dictionary parameter
    print("Hello",end=" ")              #print "Hello" and end the line with a space
    for key,value in kwargs2.items():   #For each key value in kwargs 2 item dictionary
        print(value,end=" ")            #print the value of each value from the dictionary and end with a space
                                        #the end=" " effectively paste each itteration in the same line.
#Now that we print each key value in one line using a varying dictionary we can add any number of key values we like
#and they will be printed in order.
hello2(title="Lord",first="Danish",middle="Code",Last="Monkey")

#Again, Kwargs is just the common naming the convention, the important thing is the double asterisk(**) which does all the work.