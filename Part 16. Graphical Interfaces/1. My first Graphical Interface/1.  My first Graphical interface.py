#A Graphical User Interface, or GUI for short.
#is a computer generated graphics interface a user can interact with.

#For this, we will use the Tkinter module
'''
The Tkinter module is a python binding to the Tk GUI toolkit. It is the standard Python
interface to the Tk GUI toolkit. And is Pythons de facto standard GUI
'''
#First we import:
#From Tkinter module, import *(all) to import everything
from tkinter import *

'''
A important distinction to make first, is the difference between
widgets = GUI elements: buttons, textboxes, labels, images.
windows = serves as a container to hold or contain the widgets
'''

'''---------Window----------'''
#To create a simple window, we will do the following

window_01 = Tk()                   #instantiate an instance of a window
window_01.geometry("420x420")      #set window size of window
window_01.title("My first GUI!")   #Set the window title(top, near minimize, maximize, exit buttons)
'''
In order to add a custom icon to the GUI title bar, we need to format an existing image
in this case the code monkey.png thats been added to the folder, to a photo image
that Tkinter can intrepert
'''
icon = PhotoImage(file='the_code_monkey.png')   #Create variable that holds PhotoImage function
window_01.iconphoto(True, icon)                    #set window icon to True(for custom icon) and name of PhotoImage variable
'''
Now we start configuring the inside of the window, any changes you make to the window
is done using the config function
'''
window_01.config(background="#363636") #Set background color, use either color names(black) or hex colors(#363636 for grey)


'''-------Widgets------'''
'''Widgets are the contents inside of a window'''
'''---label---'''
'''A label is an area widget that holds text and/or an image within a window'''
'''
Creating a label we will always start by assigning it a unique name, 
in this case label_01
inside the variable we will call the Label function, and inside the constructor() we will
assign the labels master, the container for the label, 
in this case window_01
with widgets in pyhton we can de-eliminate the arguments with a comma(,)
after this we can fill out whatever arguments(options) we want this widgets to have
'''
#NOTE: Good practice when using alot of arguments, is to seperate by each argument
#Lets actually generate a photoimage to use in the label, with a silly cat face!
#how lucky, the file is already in the directory, otherwise a full path would be needed.
photo_cat_face = PhotoImage(file='cat_face_meme.png')
label_01 = Label(window_01,
                 text="Hello World!",       #Text to appear
                 font=('Arial',40,'bold'),  #Font of the text
                 fg='#00FF00',              #foreground color (with hex color code)
                 bg='black',                #background color (with color name)
                 relief=RAISED,             #border style (set to RAISED)
                 bd=10,                     #Border width, set to 10 pixels
                 padx=20,                   #Add padding on x axis between text and border by 20 pixels
                 pady=10,                   #Add padding on y axis between text and border by 10 pixels
                 image=photo_cat_face,      #add the photo_cat_face PhotoImage to the label
                 compound='bottom'          #place the image on the bottom of the label
                 )                          #end with )
'''
now to actually make the label APPEAR in the window, we will need to actually
add the label to the window.
One way which we can do that is with a pack function
'''

label_01.pack() #variable name label_01, pack to master
'''
Another way to add a widget to a window, is with the place function
This will allow us to define where we want the widget to appear within the window.
'''
#The place function will place the widget on the given x,y pixel coordinate of the window from the top left.
#this will for instance place the widget on the top left.
#label_01.place(x=0,y=0)

'''Buttons!'''
'''You click them, they do something. Amazing!'''
#For this button, we will be using a function, so we will just define that real quick
#This will execute when the button is pressed
#it will count the amount of times it has been pressed, and print BOOM! to console
#to make a counter, we need a variable to house the count starting at 0
button_count = 0
def boom():
    global button_count
    button_count+=1
    print("BOOM! "+ str(button_count))
#Now when the button is pressed it will perform what is called a callback
#by having a function outside of the button that the button calls-back-to

#We will also use a image in the button! So another Photoimage
photo_bomb_man = PhotoImage(file='bombman.png')
'''The formatting of a button is exactly like a label'''
'''Syntax (button name) = Button(Master, arg/option 1, arg/option 2, ,etc, etc2, etc3)'''
button_01 = Button(window_01,               #master, the container to place the button
                   text="Clik meh!",        #place some text in the button
                   command=boom,            #callback to the boom function
                   font=("Comic Sans",30),  #font of the text in the button
                   fg=("white"),            #Foreground color, with hext color code
                   bg="black",              #Background color, with color name
                   activeforeground="#00FF00",  #foreground color, when button is hovered or pressed
                   activebackground="black",     #background color, when button is hovered or pressed
                   state=ACTIVE,            #Sets the state functionality of a button, if DISABLE then button wont do anything
                   image=photo_bomb_man,
                   compound='left'
                   )
button_01.pack()
#Finally, once we are satisfied, we place the window on the screen.
window_01.mainloop()                   #place window on computer screen, and listen for events
