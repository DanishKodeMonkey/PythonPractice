'''
A frame is a rectangular container to group and hold widgets.
Useful to keep a group of widgets together, and place the container itself including
all the widgets around on the window.
'''

from tkinter import *

window_01 = Tk()                #Create new window called window_01 using Tk

frame_01 = Frame(window_01,     #Create new frame called frame_01, using Frame function of Tkinter, assign to window_01
                 bg="black",    #Change background to black color
                 bd=5,          #set border of frame to 5 pixels
                 relief=RAISED) #Set style of border to RAISED
frame_01.place(x=10, y=10)      #place frame_01 at window coordinates 10,10

#You can create a button or other widget without assigning it to a variable,
#useful for short and sweet widget creations, but you cant change it later in the code.
Button(frame_01, text = "W", font= ("Consolas", 25), width=3).pack(side=TOP)    #Create new button, assign to frame 01 and pack immediately, placing it to the top of the frame
Button(frame_01, text = "A", font= ("Consolas", 25), width=3).pack(side=LEFT)   #Repeat, but pack on the left side of the frame
Button(frame_01, text = "S", font= ("Consolas", 25), width=3).pack(side=LEFT)   #repeat, but pack on the left side, after the previous define button
Button(frame_01, text = "D", font= ("Consolas", 25), width=3).pack(side=LEFT)   #ETC

window_01.mainloop()