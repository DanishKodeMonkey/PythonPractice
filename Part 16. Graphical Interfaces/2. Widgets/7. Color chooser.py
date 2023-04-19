from tkinter import *            #add all modules from tkinter
from tkinter import colorchooser #submodules must be added even though all other modules are added

#as always, functions first.
def click():                        #define a function called click
    color = colorchooser.askcolor() #create a variable called color, color will be whatever color is chosen with colorchooser.askcolor()
    print(color)                    #print chosen color code in RGB and hexidecimal
    window_01.config(bg=color[1])   #change configuration of window_01, change background color to value of color item 2(index 1)
    #This could all be condensed into one line of code actually
    #window.config(bg=colorchooser.askcolor()[1]) - would do the same, but does all of the above.
window_01 = Tk()

window_01.geometry("420x420")
button_01 = Button(text='click me',
                   command=click)
button_01.pack()
window_01.mainloop()
