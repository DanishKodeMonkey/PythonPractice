from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="/home/daniel/DanishKodeMonkey/Python/helloWorld/Part 16. Graphical Interfaces/3. File handling/Test folder",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All Files", ".*")
                                    ])
    if file is None:
        return
    filetext = str(text_01.get(1.0, END))
    file.write(filetext)
    file.close()

window_01 = Tk()

button_01 = Button(text='save',
                   command=saveFile
                   )
button_01.pack()

text_01 = Text(window_01)
text_01.pack()

window_01.mainloop()