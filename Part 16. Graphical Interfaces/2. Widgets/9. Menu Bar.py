'''Playing with Menus!'''

from tkinter import *

'''As usual, define functions before the window they are used in.'''
def openFile():                     #define new functioncalled openFile
    print("File has been opened")   #For the sake of testing this only prints to console
def saveFile():                     #define new function called saveFile
    print("File has been saved")    #for the sake of testing this only prints to console
def cut():                          #define new function called cut
    print("You cut some text!")     #for the sake of testing this only prints to console
def copy():                         #define new function called copy
    print("you copied some text!")  #for the sake of testing this only prints to console
def paste():                        #define new function called paste
    print("You pasted some text!")  #for the sake of testing this function only prints to console

window_01 = Tk()                    #Create new window called window_01 using Tk

#Below we use PhotoImage function to create usable images for Tk with unique variables
openImage = PhotoImage(file="funny_pictures/LOTRF.png")
saveImage = PhotoImage(file="funny_pictures/FloppyDisk.png")
exitImage = PhotoImage(file="funny_pictures/exitbyax.png")

#Here we start working on the menus in the window
#First is the bar itself, this is what spans horisontally across the window, cascade menus inside.
menubar = Menu(window_01)           #create new Menu called menubar, using Menu function. Assign to window_01
window_01.config(menu=menubar)      #configure window_01, assign menubar as window_01s menubar
fileMenu = Menu(menubar,            #Create new menu called fileMenu using Menu function, assign to menubar
                tearoff=0,          #remove tearoff(line on top of menu)
                font=("Arial",15))  #assign font and size
menubar.add_cascade(label="File",       #in menubar, add a cascade menu, assign label text "File"
                    menu=fileMenu)      #assign cascade menu to fileMenu
fileMenu.add_command(label="open",          #in fileMenu, add a command button with label "open"
                     command=openFile,      #when pressed, execute openFile function
                     image=openImage,       #add a image to the button identified as openImage
                     compound='left')       #place image to the left of the text
fileMenu.add_command(label="Save",          #in fileMenu, add a command butotn with label "save"
                     command=saveFile,      #when pressed, execute saveFile function
                     image=saveImage,       #add a image to the button called saveImage
                     compound='left')       #place added image to the left of text
fileMenu.add_separator()             #add seperator(line that seperates categories in a cascade
fileMenu.add_command(label="Exit",          #in fileMenu, add a command with the label "Exit"
                     command=quit,          #when pressed, quit program.
                     image=exitImage,       #add a image called exitImage
                     compound='left')       #place image to the left of the text

editMenu = Menu(menubar,           #Create new menu called editMenu, using Menu function, assign to menubar
                tearoff=0,         #Remove tearoff on top of menu
                font=("Arial",15)) #assign font and size
menubar.add_cascade(label="edit",  #on menubar, add a cascade menu, labeled "edit"
                    menu=editMenu) #assign to editMenu
editMenu.add_command(label="Cut",       #on editMenu, add command button labeled "Cut"
                     command=cut)       #When pressed, execute cut function
editMenu.add_command(label="Copy",      #on editMenu, add command button labeled Copy
                     command=copy)      #when pressed, execute copy function
editMenu.add_command(label="Paste",     #on editmenu, add command button labeled paste
                     command=paste)     #when pressed ,execute paste function
window_01.mainloop()    #finally display window on screen!
