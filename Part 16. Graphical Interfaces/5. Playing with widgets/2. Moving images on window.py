from tkinter import *

def move_up(event):
    label_01.place(x=label_01.winfo_x(),y=label_01.winfo_y()-10)
def move_down(event):
    label_01.place(x=label_01.winfo_x(),y=label_01.winfo_y()+10)
def move_left(event):
    label_01.place(x=label_01.winfo_x()-10,y=label_01.winfo_y())
def move_right(event):
    label_01.place(x=label_01.winfo_x()+10,y=label_01.winfo_y())
window_01 = Tk()
window_01.geometry("500x500")
window_01.config(bg="white")

window_01.bind("<w>",move_up)
window_01.bind("<s>",move_down)
window_01.bind("<d>",move_right)
window_01.bind("<a>",move_left)

heli = PhotoImage(file='/home/daniel/DanishKodeMonkey/Python/helloWorld/Part 16. Graphical Interfaces/2. Widgets/funny_pictures/heli.png')
label_01 = Label(window_01, image=heli)
label_01.place(x=0,y=0)

window_01.mainloop()