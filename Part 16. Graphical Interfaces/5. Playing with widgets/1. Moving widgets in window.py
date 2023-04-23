from tkinter import *

'''as an experiment, lets try and make 2 labels movable in the window they are stored in'''

'''To do this we will need 2 functions, and 2 bindings'''
#remember, that the "event" in functions are what is called in the bind, whichever button is used.
def drag_start(event):          #define function called drag_start
    widget = event.widget       #get the name of the widget interacted with, and nickname it widget
    widget.startx = event.x     #Get the point within the widget that is clicked x axis
    widget.starty = event.y     #Get the point within the widget that is clicked y axis
    #We now know where in the label we click
def drag_motion(event):         #Define a new function called drag_motion, with the event parameter
    widget = event.widget   #get the name of the widget the event is happening to, and nickname it widget
    x = widget.winfo_x() - widget.startx + event.x #variable x is the widgets location, minus its starting position, + its movement
    y = widget.winfo_x() - widget.starty + event.y#same, but for y
    widget.place(x=x,y=y)   #Set widget placement to variable x and y

window_01 = Tk()

label_01 = Label(window_01,bg="red",width=10, height=5)
label_01.place(x=0,y=0)

label_02 = Label(window_01,bg="blue",width = 10, height = 5)
label_02.place(x=100, y=100)

label_02.bind("<Button-3>",drag_start)
label_02.bind("<B3-Motion>",drag_motion)

label_01.bind("<Button-1>",drag_start)
label_01.bind("<B1-Motion>",drag_motion)

window_01.mainloop()