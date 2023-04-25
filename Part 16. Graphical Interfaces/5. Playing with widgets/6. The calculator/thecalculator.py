from tkinter import *

def button_press(num):           #Define function called button_press that accepts 1 parameter(num)

    global equation_text #Grab equation_text from global

    equation_text = equation_text + str(num)    #Equation text is a variable that holds equation text + string of input value
    equation_label.set(equation_text)           #change equation_label text to equation_text

def equals():   #define new function called equals
    global equation_text    #grab equation_text from global

    try:        #Within a try loop

        total = str(eval(equation_text))    #Set the total to the string of evaluation of equation_text

        equation_label.set(total)           #set equation_label text to totals value

        equation_text = total               #In order to re-use the result from a previous calculation, set equation_text to total

    except ZeroDivisionError:       #If we encounter exception ZeroDivisionError
        equation_label.set("Cannot divide by 0")    #Set Equation_label to "cannot divide by 0"
        equation_text = ""                          #clear equation text
    except SyntaxError:             #If we encounter exception SyntaxError
        equation_label.set("Syntax error...")   #set equation_label to "Syntax error..."
        equation_text = ""                      #clear equation_text

def clear():                #define new function called clear
    global equation_text    #Grab equation_text from global

    equation_label.set("")  #set equation_label to ""(empty)
    equation_text = ""      #set equation_text to ""(empty)

window_01 = Tk()
window_01.title("Calculator program")
window_01.geometry("500x600")

equation_text = ""

equation_label = StringVar()

label_01 = Label(window_01, textvariable=equation_label, font=('Mononoki Nerd Font',20),bg="white",width=24, height=2)
label_01.pack()

frame_buttons = Frame(window_01)
frame_buttons.pack()

#button 1, holding the press of 1. Copy pasta this several times with 1-9+0
#with the only difference being clear and equals that has command to the function
button1 = Button(frame_buttons, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame_buttons, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame_buttons, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame_buttons, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame_buttons, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame_buttons, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame_buttons, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame_buttons, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame_buttons, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame_buttons, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3,column=0)

buttonplus = Button(frame_buttons, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
buttonplus.grid(row=0,column=3)

buttonminus = Button(frame_buttons, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('-'))
buttonminus.grid(row=1,column=3)

buttonmultiply = Button(frame_buttons, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'))
buttonmultiply.grid(row=2,column=3)

buttondivide = Button(frame_buttons, text='/', height=4, width=9, font=35,
                 command=lambda: button_press('/'))
buttondivide.grid(row=3,column=3)

buttonequal = Button(frame_buttons, text='=', height=4, width=9, font=35,
                 command=equals)
buttonequal.grid(row=3,column=2)

buttondecimal = Button(frame_buttons, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'))
buttondecimal.grid(row=3,column=1)

buttonclear = Button(window_01, text='clear', height=4, width=12, font=35,
                 command=clear)
buttonclear.pack()

window_01.mainloop()