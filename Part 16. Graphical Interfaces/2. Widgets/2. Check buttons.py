from tkinter import *

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You dont agree? :(")
window_01 = Tk()

x = IntVar()

agent_photo = PhotoImage(file='funny_pictures/cartoon_agent.png')

check_button_01 = Checkbutton(window_01,
                              text="I agree to something",
                              variable=x,
                              onvalue=1,
                              offvalue=0,
                              command=display,
                              font=('Arial',20),
                              fg="#00FF00",
                              bg="black",
                              activeforeground="#00FF00",
                              activebackground="black",
                              padx=25,
                              pady=10,
                              image=agent_photo,
                              compound=LEFT,3.
                              )
check_button_01.pack()

window_01.mainloop()