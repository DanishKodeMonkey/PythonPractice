from tkinter import *

def create_window():
    #new_window = Toplevel() #Toplevel() = A new window 'on top' of other windows, linked to a 'bottom' window
                            #should the bottom(first) level window close, the top ones close with them in a cascade
    new_window = Tk()       #Tk() = New independent window
    window_01.destroy()     #close defined window, in this case, window_01
window_01 = Tk()

Button(window_01, text="Create new window", command=create_window).pack()

window_01.mainloop()