'''
We can bind a key event to a widget or a window, so that when we press a certain
key, or do something, we can trigger a function.
'''
from tkinter import *

#Windows and widgets have access to a bind function, these handle assigning
#a function to a key.

#function to call further below.
def doSomething(event):     #Define new function called doSomething with a parameter called event(important, remember that)
    #print("You pressed: "+event.keysym)#when called, print you did a thing
    label_01.config(text=event.keysym)

window_01 = Tk()

window_01.bind("<Key>", doSomething)  #in window_01, bind q(remember "<>" when calling keys), when pressed, execute doSomething
label_01 = Label(window_01,font=("Helvetica",100))  #Create label, and assign to window_01
label_01.pack()#place label_01 in window

window_01.mainloop()