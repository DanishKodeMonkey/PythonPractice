#The canvas is a widget that is used to draw graphs, plots, and images in a window

from tkinter import *

window_01 = Tk()

canvas = Canvas(window_01,
                height = 500,
                width = 500)
#Some various examples of shapes used in the canvas
'''
canvas.create_line(0,0,500,500,
                   fill="blue",
                   width=5)
canvas.create_line(0,500,500,0,
                   fill="red",
                   width=5)
canvas.create_rectangle(50,50,250,250,
                        fill="yellow")
points=[250,0,500,500,0,500]
canvas.create_polygon(points,
                      fill="purple",
                      outline="black",
                      width=5)
canvas.create_arc(0,0,500,500,
                  #style=PIESLICE(default)/CHORD/ARC,
                  start=90,
                  extent=180,
                  fill="blue")
'''
#Heres a pokeball!
'''
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width=10)
canvas.pack()
'''
canvas.create_oval(10,10,490,490,fill="yellow",width=10)
canvas.create_arc(30,250,250,30,fill="black",extent=180,start=180)
canvas.create_arc(470,250,250,30,fill="black",extent=180,start=180)
canvas.create_arc(100,350,350,300,style=ARC,fill="black",width=10,extent=180,start=180)
canvas.pack()

window_01.mainloop()