from tkinter import *

def move_up(event):
    canvas_01.move(myheli,0,-10)
def move_down(event):
    canvas_01.move(myheli, 0, 10)
def move_left(event):
    canvas_01.move(myheli, -10, 0)
def move_right(event):
    canvas_01.move(myheli, 10, 0)

window_01 =Tk()

window_01.bind("<w>",move_up)
window_01.bind("<a>",move_left)
window_01.bind("<s>",move_down)
window_01.bind("<d>",move_right)

canvas_01 = Canvas(window_01,width=500,height=500)
canvas_01.pack()

heli = PhotoImage(file='/home/daniel/DanishKodeMonkey/Python/helloWorld/Part 16. Graphical Interfaces/2. Widgets/funny_pictures/heli.png')
myheli = canvas_01.create_image(0,0,image=heli,anchor=NW)

window_01.mainloop()