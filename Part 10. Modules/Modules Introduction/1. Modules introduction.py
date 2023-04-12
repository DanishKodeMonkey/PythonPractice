#modules are files that contain python code. They may contain functions, classes and more.
#They are used with modular programming ,which is to seperate a program into parts.
#You can import built in modules like os, random, math etc. Or you can create your own in a project and import them.
#See messages.py for more on creating modules.

#Here we will import whatever has been made in the messages.py module
#For easier access, we can nickname a module in here by using "as"
import messages as msg #Import the messages module, arguably the safest approach to importing to avoid naming conflicts.



#To use a function of a module, type the name of the module, then the name of the function within the module
msg.hello()
msg.bye()

#You can also import specific functions and classes from a module by using "from"
from messages import hello,bye

#Or you can use asterisk(*) to import all contents from the module.
#This is not recommended for large programs however as it can result in naming conflicts.

from messages import *
#Doing this will let you use the functions and classes directly without refering to the module

hello()
bye()
