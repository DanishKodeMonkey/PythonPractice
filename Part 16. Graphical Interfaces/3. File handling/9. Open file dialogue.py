from tkinter import *
from tkinter import filedialog
def openFile():
    # Call filedialog.askopenfilename function. Returns string, with initialdir argument set to where the file path starts.
    filepath = filedialog.askopenfilename(initialdir='\\home\\daniel\\DanishKodeMonkey\\Python\\helloWorld\\Part 16. Graphical Interfaces\\2. Widgets',
                                          title="Open file okay?",   #set title of file path dialog
                                          filetypes=(("text files","*.txt"),    #Set prefered file type
                                          ("all files","*.*")))                 #set alternate file type(all files)

    file = open(filepath, 'r')                     #open filepath, using r for read(or rt for read text, or rb for read binary) assign to file
    print(file.read())                             #print the contents of the file through (variable name).read()
    file.close()                                   #remember to close a file after use!

window_01 = Tk()

button_01 = Button(text="Open", command=openFile)
button_01.pack()


window_01.mainloop()