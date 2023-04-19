from tkinter import *

'''
ENTRY WIDGET
a textbox that accepts a single line of user input
'''
#First we create a new window, lets go ahead and play with some arguments again
    #Below are the functions used inside the window
def submit():                       #Define function called submit
    username = entry_01.get()       #create variable called username, extract input from entry_01 with get function
    print("Hello "+username)        #print "Hello (whatever was input in entry_01)"
    entry_01.config(state=DISABLED) #Disable text box after submitting and grey it out

def delete():               #Define function called delete
    entry_01.delete(0,END)  #when delete is executed, take whatever content is in entry_01 and delete from index 0 to the end

def backspace():
    '''
    This one is a bit longer.
    To delete only the first letter of the entry we will have to first
    find out how long the entry is, and delete the last index of that length, towards the end of the entry
    '''
    entry_01.delete(len(entry_01.get())-1, END)
window_01 = Tk()                    #Create a window called window_01 using Tkinter

entry_01 = Entry(window_01,         #Create a Entry widget called entry_01 with some arguments
                 font=("Arial",50), #set font inside entry widget to Arial size 50
                 fg="#00FF00",      #Set foreground color of entry widget to hex value
                 bg="black",        #Set background color of entrybox to black
                 #show="*"          #If we wanted to replace all entry characters, use show.
                                    # Useful for something like passwords,
                                    # it will still submit what you actually type into console
                 )
#to place some default text in the text box, you can use the insert function
entry_01.insert(0, 'Please enter name')
entry_01.pack(side=LEFT)      #place entry_01 into its master on the left with pack function

#now lets make a button to actually submit whatever the user types into the entry widget

submit_button_entry_01 = Button(window_01,      #Create a submit button, assign to window_01
                                text="submit",  #text to display in button
                                command=submit  #function to execute when button is pressed(callback)
                                )
submit_button_entry_01.pack(side=RIGHT)         #place button inside master on the right side

delete_button_entry_01 = Button(window_01,      #Create a button and assign it to window_01
                                text="delete",  #write text inside button
                                command=delete  #Execute command once button is pressed(callback)
                                )
delete_button_entry_01.pack(side=RIGHT)         #add button to master window on the right side

backspace_button_entry_01 = Button(window_01,      #Create a button and assign it to window_01
                                text="backspace",  #write text inside button
                                command=backspace  #Execute command once button is pressed(callback)
                                )
backspace_button_entry_01.pack(side=RIGHT)         #add button to master window on the right side


window_01.mainloop()