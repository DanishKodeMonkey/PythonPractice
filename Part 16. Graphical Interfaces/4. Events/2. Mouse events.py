from tkinter import *
'''Like key events, mouse events can be bound to a function in a window
or widget, main difference being that a mouse key has various states to bind.
and interacts with the window or widget.'''
def doSomething(event):
    print("You clicked at: " + str(event.x)+","+str(event.y))

window_01 = Tk()

window_01.bind("<Button-1>",doSomething) #left mouse click
window_01.bind("<Button-2>",doSomething) #scroll wheel
window_01.bind("<Button-3>",doSomething) #right mouse click
window_01.bind("<ButtonRelease>",doSomething) #execute on button release
window_01.bind("<Enter>",doSomething)  #Enter the window
window_01.bind("<Leave>",doSomething) #leave the window
window_01.bind("<Motion>",doSomething) #Where the mouse moved

window_01.mainloop()