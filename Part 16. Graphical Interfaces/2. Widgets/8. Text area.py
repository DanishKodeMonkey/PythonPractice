'''
A text widget is like a text area, you can enter multiple lines of text
'''

from tkinter import *

#as always, functions first.
def submit():                       #define a function called submit
    input = text_01.get("1.0", END) #when executed, create a variable called input, get the text from text_01 line 1.0 to the end
    print(input)                    #print input variable to console

window_01 = Tk()            #create a new window, called window_01, using Tk

text_01 = Text(window_01,                   #create a text field called text_01, assign to window_01
               bg="light yellow",           #set background color to light yellow
               font=("Ink Free", 25),       #set font to "ink free" if installed on computer, size 25
               height=8,                    #set height of text field to 8
               width=20,                    #set width of text field to 20
               padx=20,                     #add padding of 20 pixels to x axis
               pady=20,                     #add padding of 20 pixels to y axis
               fg="purple"                  #set foreground color to purple
               )
text_01.pack()                              #add text field to window
button_01 = Button(window_01,text="submit", command=submit) #create new button call--- you know this..
button_01.pack()

window_01.mainloop()          #finally, show the window on screen