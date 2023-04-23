from tkinter import *
from time import *

'''Lets make a clock!'''
'''For this we will need a recursive function'''
'''A recursive function, is a function that repeats itself:'''
def update():           #Define new funciton called update
    time_string = strftime("%I:%M:%S %p")   #Create variable called time_string, which is function strftime(Hour,Minute,seconds, am/pm)
    time_label.config(text=time_string)     #configure label time_label with text form time_string(strftime returns a string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window_01.after(1000,update)  # after performing window_01 tasks, wait 1000 milliseconds, then run update again.(this is where its recursive)


window_01 = Tk()

time_label = Label(window_01, font=("Arial",50),fg='#00FF00',bg="black")
time_label.pack()

day_label = Label(window_01, font=("Ink Free",25),fg='#00FF00',bg="black")
day_label.pack()

date_label = Label(window_01, font=("Ink Free",30))
date_label.pack()
update()

window_01.mainloop()