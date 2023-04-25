#for this program we will need a array of different imports

import os #for interacting with the operating system
from tkinter import * #for using the tkinter gui package
from tkinter import filedialog, colorchooser, font #Specifically importing some extra modules
from tkinter.messagebox import * #Import functions from tkinter.messagebox module
from tkinter.filedialog import *  #import functions from tkinter.filedialog module

#Functions will be folded, press ... to unfold
def change_color(): #Define a function called change_color
    #when called:
    color = colorchooser.askcolor(title="pick a color you MONKEY") #new variable color executes colorchooser.askcolor with a title
    #print color to console, this goes to show that colorchooser.askcolor returns a tuple. We need the 2nd value
    text_area.config(fg=color[1]) #configure the text area, change foreground color to index 1 of the color variable

def change_font(*args): #define function called change_font, that accepts a number of arguments (since we will accept both font_name and font_size)
    #Configure text area, set font to whatever font_name is, and font size to whatever size_box is
    text_area.config(font=(font_name.get(),size_box.get()))

def new_file(): #Define new function called new_file
    window.title("Untitled")    #Set the title of the window to "untitled
    text_area.delete(1.0,END)   #Delete whatever text is in the text_area

def open_file():            #define new function called open_file
    #define variable called file
    #which prompts a askopenfilename function, with the default extentions set, and filetypes set
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                            ("Text Documents", "*.txt")])
    #After finishing that,
    try: #try the following:
        #set window.title to the os.path that the file was opened from
        window.title(os.path.basename(file))
        #delete whatever text was already in the text_area
        text_area.delete(1.0,END)
        #define a variable called file, which is whatever file was selected earlier
        #open the file, and read it(r)
        file = open(file, "r")
        #After reading the file, insert whatever we read into the text_area from the start
        text_area.insert(1.0, file.read())
    #if any exception occours
    except Exception:
        #print "Could not read file"
        print("Could not read file")
    #Finally, no matter what happens before now
    finally:
        #close the file.
        file.close()

def save_file():        #define a function called save_file
    #similar process to opening a file, this time we prompt for a place to SAVE the file
    file = filedialog.asksaveasfilename(initialfile="untitled.txt",
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents","*.txt")])
    #If nothing is chosen, do nothing
    if file is None:
        return
    else: #Otherwise
        try: #Try the following:
            #Set window.title to the path name we chose before
            window.title(os.path.basename(file))
            #open the selected file, and write(w)
            file = open(file,"w")
            #when writing, get the text_area text from start till end
            file.write(text_area.get(1.0,END))
        #if any exception happens
        except Exception:
            print("Couldnt save file :(")
        finally:    #Finally, no matter what else happens here
            file.close()    #close the file

def cut():
    #The cut, copy and paste functions are pretty similar,
    #we simply call a event already found in the os module
    #within the text_area
    text_area.event_generate("<<Cut>>")

def copy():
    # The cut, copy and paste functions are pretty similar,
    # we simply call a event already found in the os module
    # within the text_area
    text_area.event_generate("<<Copy>>")

def paste():
    # The cut, copy and paste functions are pretty similar,
    # we simply call a event already found in the os module
    # within the text_area
    text_area.event_generate("<<Paste>>")

def about():
    #open a info prompt with this text. With a title, and text.
    showinfo("About this program","Danish Kode Monkey was here!")

def quit():
    #just close the window we created
    window.destroy()

window = Tk()   #So, create a window
window.title("DKM text editor program!")    #Set a title
file = None   #define a variable called file, and for now, set it to None
#ocnfigure the window
window_width = 500
window_height = 500

#fetch the size of the screen the program is used on
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
#define x and y, and set them to half the amount of pixels that screen width and height it
#effectively finding the center of the screen
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

#set the windows geometry to the size we defined with width and height
#and place it in the center coordinates we found just before
window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

#define a variable called font_name, that consist of a string variable, assign to window
font_name = StringVar(window)
#Set a default font
font_name.set("Mononoki Nerd Font")

#define a variable called font_size, that consist of a stringvariable, assigned to window
font_size = StringVar(window)
#set default font size
font_size.set("25")

#create a text area, assign it to window, and set the font to whatever font_name and font_size is set to
text_area = Text(window, font=(font_name.get(),font_size.get()))

#add a scroll bar, assign to the text area
scroll_bar = Scrollbar(text_area)
#ensure the text area fills out the window.
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N + E + S + W)
#pack up the scroll bar, and place it on the right, and fill out the Y axis
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

#create a frame, and assign it to window
frame = Frame(window)
#create a grid in the frame
frame.grid()

#in the frame, create a button called color_button, and assign it a function defined at the top
#of the program, and place it in grid 0,0
color_button = Button(frame,text="color",command=change_color)
color_button.grid(row=0,column=0)

#etc
font_box = OptionMenu(frame, font_name, *font.families(),command=change_font)
font_box.grid(row=0, column=1)

#etc
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0,column=2)

#Create a menu bar, assign it to the window
menu_bar = Menu(window)
window.config(menu=menu_bar)

#create a menu called file_menu, add it to the menu_bar, remove the tearoff.
file_menu = Menu(menu_bar, tearoff=0)
#add a cascade menu to the file_menu in the menu_bar
menu_bar.add_cascade(label="File",menu=file_menu)
#add various command buttons to the cascade window
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
#add a seperator(just a line)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit)

#etc
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_command(label="Paste",command=paste)

#etc
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()