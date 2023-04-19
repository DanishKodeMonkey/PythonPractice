from tkinter import *
from tkinter import messagebox #import the messagebox library

#below we define a multitude of different message boxes, uncomment the one you want to see
#they all share similar approaches, some have returns, that can be used in a if statement
def click():
        #basic messagebox, info
    #messagebox.showinfo(title = 'This is a info message box', message = 'You are a person!')

        #basic messagebox, warning
    #messagebox.showwarning(title = 'WARNING!', message = 'This is a warning!')

        #basic messagebox, error
    #messagebox.showerror(title = 'Error', message = 'Something went wrong')

        #3 choice messagebox, askokcancel, returns True/False/None to use in if statement
    #if messagebox.askokcancel(title = 'ask ok cancel', message='do you want to do the thing?'):
    #    print('you did a thing!')
    #else:
    #    print('you canceled a thing! :(')

        #3 choice messagebox, returns True/False/None to use in if statements
    #  if messagebox.askretrycancel(title = 'ask retry cancel', message='do you want to retry the thing?'):
    #     print('you retried a thing!')
    #  else:
    #     print('you canceled a thing! :(')

        #3 choice messagebox, returns True/False/None to use in statements
    #if messagebox.askyesno(title='ask yes or no', message='do you like coffee?'):
    #    print('I like coffee too!')
    #else:
    #    print('You lie!')

        #3 choice messagebox, returns STRING yes/no
    #answer = messagebox.askquestion(title='ask question', message='do you like tea?')
    #if(answer == 'yes'):
    #    print("Ew")
    #else:
    #    print('Good, you should try coffee!')

        #3 choice messagebox, returns True/False/None
    #answer = messagebox.askyesnocancel(title='yes no cancel',message='Do you like to code?')
    #if(answer == True):
    #    print("You like to code")
    #elif(answer==False):
    #    print("You dont like to code")
    #else:
    #    print("You dodge the question? :(")

#Furthermore you can replace the icon used in any message box with any of these preset ones
#icon= warning/info/error

window_01 = Tk()                #Create a new window called window_01 using Tk

button_01 = Button(window_01,       #create new button called button_01, assign to window_01
                   command=click,   #once pressed, execute click function
                   text='click me') #set text on button to "click me"
button_01.pack()                    #add button to window.

window_01.mainloop()               #Finally, show the window on screen