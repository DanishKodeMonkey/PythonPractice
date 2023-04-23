'''
A grid gemoetry manager organises widgets in a table-like structure in a parent
similar to a spread sheet wit hrows and columns
'''
from tkinter import *

'''
For this example we will create a simple submission form using this method.
'''

window_01 = Tk()        #Create new window called window_01, using Tk

'''
Create new label called firstNameLabel, assign to window_01, with text, and
instead of pack, which places all widgets below each other horisontally in order that
they are packed.
we use grid, and define which row and column we want it placed in relation to other widgets
in the same window
'''
'''
Observe how changing the width of a widget in a row, adjusts the entire row to match said width
'''
titleLabel = Label(window_01,text="Enter your info",font=("Arial", 25)).grid(row=0,column=0)

firstNameLabel = Label(window_01, text= "first name: ",width=20, bg="red").grid(row=1,column=0)#<--Place in row 0, column 0, top left
firstNameEntry = Entry(window_01).grid(row=1,column=1)  #<-- Place in row 0, column 0, right of firstNameLabel

lastNameLabel = Label(window_01, text="last name: ",bg="green").grid(row=2,column=0)
lastNameEntry = Entry(window_01).grid(row=2,column=1)

emailLabel = Label(window_01, text="email: ",bg="blue",width = 30).grid(row=3, column=0)
emailEntry = Entry(window_01).grid(row=3,column=1)

submitButton = Button(window_01, text="Submit").grid(row=4,column=0, columnspan=2)


window_01.mainloop()