from tkinter import *

def submit():
    print("the temperature is: "+str(scale_01.get())+" degrees C")
window_01 = Tk()

#add a image of a hot fire to the top of the window by placing it here, above the
#code for the slider itself, inside a label.
hotImage = PhotoImage(file='funny_pictures/superhotfire.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale_01 = Scale(window_01,                 #Create a scale widget, and assign to master window_01
                 from_=100, to=0,           #define the range of the scale, NOTE: always have "_" in from
                 length=600,                #Length of the scale in pixels
                 orient=VERTICAL,           #Specify orientation of scale(Default = VERTICAL)
                 font = ('Consolas', 20),   #Set the font
                 tickinterval = 10,         #numeric indicators every 10th value of the scale
                 showvalue = 1,             #shows the value that sits ON the slider in the scale
                 resolution = 5,            #Increment of the slider value
                 troughcolor = '#69EAFF',    #Set color of slide trough(the background of the slide "track"?
                 fg = '#FF1C00',            #foreground color, set to a hot red
                 bg = 'black',              #background color, set to black.
                 )
#scale.set(50)   #Set the starting position of the slider on the scale
'''
A more sophisticated way of making sure the slider always starts in the middle
is using a formula
'''
#NOTE: This formular is REUSABLE TO ANY SCALE! WOOO COPY PASTA!
scale_01.set(((scale_01['from']-scale_01['to'])/2)+scale_01['to'])
scale_01.pack()

#Add a image of a icecrea(so funny) below the scale by placing it here, after the code
#for the scale itself!
#But BEFORE the button, so the button appears last!
coldImage = PhotoImage(file='funny_pictures/icecicle.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()
button_01 = Button(window_01,
                   text = 'submit',
                   command=submit
                   )
button_01.pack()

window_01.mainloop()