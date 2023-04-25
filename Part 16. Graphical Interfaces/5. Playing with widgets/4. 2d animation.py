from tkinter import *

import time

'''SO lets start by making some variables'''
#A thing of note, common naming convention dictates that CONSTANTS, as in variables and attributes
#that we dont plan on changing, are named in all caps
WIDTH = 500             #We will make a variable called WIDTH, and set it at 500
HEIGHT = 500            #We will make a variable called HEIGHT, and set it at 500
xVelocity = 2           #we will make a variable called xVelocity, set at 2
yVelocity = 3           #and yVelocity, set at 3

window = Tk()               #Create a window called window using Tk function
window.config(bg="white")   #configure window, make background white(deprecated due to background image)

canvas = Canvas(window, width=WIDTH, height=HEIGHT) #make a canvas, assign it to window, with the constants set as width and height
canvas.pack() #place canvas on window

#make a photoimage from a file, name it cloud_image
cloud_image = PhotoImage(file='/home/daniel/DanishKodeMonkey/Python/helloWorld/Part 16. Graphical Interfaces/2. Widgets/funny_pictures/skyline.png')
#create a canvas called background, and place a image called cloud_image at coords 0,0 anchored northwest
background = canvas.create_image(0,0,image=cloud_image,anchor=NW)

#make a photoimage from a file, name it heli_image
heli_image = PhotoImage(file='/home/daniel/DanishKodeMonkey/Python/helloWorld/Part 16. Graphical Interfaces/2. Widgets/funny_pictures/heli.png')
#make a canvas called my_heli, place a image at coords 0,0 using the heli_image PhotoImage, anchor to northwest corner
my_heli = canvas.create_image(0,0,image=heli_image,anchor=NW)


#define the width, and height of the heli_image, and assign them to variables image_width, image_height
image_width = heli_image.width()
image_height = heli_image.height()
while True: #while true, or while program is running
    coordinates = canvas.coords(my_heli)   #get coordinates of image
    print(coordinates)                      #print coordinates to console
    if (coordinates[0] >= WIDTH-image_width or coordinates[0] < 0): #if coordinates element 0(x axis) is greater than canvas width, or less than 0
        xVelocity = -xVelocity                          #set xvelocity to be negative xVelocity(reverse)
    if (coordinates[1] >= HEIGHT - image_height or coordinates[1] < 0):  # if coordinates element 1(y axis) is greater than canvas width, or less than 0
        yVelocity = -yVelocity  # set yVelocity to be negative yVelocity(reverse)
    canvas.move(my_heli,xVelocity,yVelocity)                    #move canvas called my_heli, by xvelocity and yvelocity
    window.update()                         #update window for any changes
    time.sleep(0.01)                        #wait for 0.01 seconds

window.mainloop()