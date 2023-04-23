from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar_01['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window_01.update_idletasks()

window_01 = Tk()

percent = StringVar()
text = StringVar()

bar_01 = Progressbar(window_01,
                     orient=HORIZONTAL,
                     length=300
                     )
bar_01.pack(pady=10)

percentLabel = Label(window_01, textvariable=percent).pack()
taskLabel = Label(window_01,textvariable=text).pack()
button_01 = Button(window_01,
                   text="download",
                   command=start).pack()


window_01.mainloop()