'''Listbox a listing of selectable text items within its own container'''

from tkinter import *

#Functions to be used with the listbox go first, before the window is created.
def submit():           #Define a function called submit
    food=[]                                 #create a list called food
    for index in listbox_01.curselection(): #for each item selected in listbox_01
        food.insert(index,listbox_01.get(index))#run the insert command from food, for each selected item, to the listbox
    print("You have ordered: ") #When called, the submit function prints you have ordered
    for index in food:
        print(index)

def add():              #Define a function called add
    listbox_01.insert(listbox_01.size(),entryBox.get()) #When called, the function gets the item entered in entryBox, and paste it in listbox_01
    listbox_01.config(height=listbox_01.size())         #then it changes a configuation, adjusting the height of the listbox, to the current size of the listbox

def delete():           #Define a function called delete
    for index in reversed(listbox_01.curselection()):   #for index in REVERSED order of selection in listbox_01
        listbox_01.delete(index)                        #delete index, this is done to accomidate the change in indexes when deleted.
    listbox_01.config(height=listbox_01.size())     #afterwards, it will adjust the height, to the new size of listbox_01


window_01 = Tk()                                #Create a window called window_01 using Tk

listbox_01 = Listbox(window_01,                 #Create a new Listbox called listbox_01, and assign it to window_01
                     bg="#f7ffde",              #change the background color
                     font=("Constantia",35),    #change the font
                     width=12,                   #assign a width of 12 pixels to the listbox
                     selectmode=MULTIPLE       #set selectmode to multiple, to allow multiple choices to be selected at once
                     )
listbox_01.pack()                               #add the listbox to the window

listbox_01.insert(1,"pizza")                    #insert item index 1 into listbox_01
listbox_01.insert(2,"pasta")                    #insert item index 2 into listbox_01
listbox_01.insert(3,"garlic bread")             #insert item index 3 into listbox_01
listbox_01.insert(4,"soup")                     #insert item index 4 into listbox_01
listbox_01.insert(5,"salad")                    #insert item index 5 into listbox_01

listbox_01.config(height=listbox_01.size())     #change listbox_01 configuration: height, to the current size of the listbox

entryBox = Entry(window_01)                     #create a new entrybox called entryBox, assign it to window_01
entryBox.pack()                                 #add the entryBox to window_01

submitButton = Button(window_01,                #create a new button called submitButton, assign it to window_01
                      text="submit",            #change the text inside the button to submit
                      command=submit,           #set the command when the button is pressed, to execute submit function
                      )
submitButton.pack()                             #add the submit button to window_01
addButton = Button(window_01,                   #Create a new button called addbutton, assign it to windows_01
                      text="add",               #set the text on the button to "add"
                      command=add               #set the command to execute when pressed to execute add function
                      )
addButton.pack()                                #add the button to window_01


deleteButton = Button(window_01,                #create a new button called deleteButton, assign to window_01
                      text="delete",            #set the text on the button to "delete"
                      command=delete            #set the command of the button to execute delete function when pressed
                      )
deleteButton.pack()                             #add button to window_01

window_01.mainloop()                            #finally, show the window on screen.