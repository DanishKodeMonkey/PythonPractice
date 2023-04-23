from tkinter import *
'''In order to work with tabs we also need the expanded Tkinter module, called ttk'''
from tkinter import ttk

window_01 = Tk()

notebook_01 = ttk.Notebook(window_01) #Widget that manages a collection of windows and displays

tab_01 = Frame(notebook_01)         #A new frame for tab 1
tab_02 = Frame(notebook_01)         #A new frame for tab 2

notebook_01.add(tab_01, text="Tab 1")   #add tab 1 to notebook 1
notebook_01.add(tab_02, text="Tab 2")   #add tab 2 to notebook 1
notebook_01.pack(expand = True,         #Place notebook_01 in window, expand to auto adjust to window size
                 fill="both")           #will fill space on x and y axis, effectively expanding to fit the entire window.

Label(tab_01, text="Hello, this is tab_01", width = 50, height = 25).pack()#Create simple label in tab_01
Label(tab_02, text="Hello, this is tab_02", width = 50, height = 25).pack()#creat simple label in tab_02



window_01.mainloop()