
'''import the Simple Mail Transfer Protocol LIBrary'''
import smtplib

'''To start, we will set up variables holding different values that we will use'''
sender = "humberjini@gmail.com"
receiver = "daniel_runge_@hotmail.com"
#remember to delete password after test.
password = "5X@i828QhBbdkJ!$fQR@!cs@AXmpb2XyZQ6P2CSFNUpTunybvn#CvW4ZfYv7&b"
subject = "Python email test"
body = "I wrote an email using Python!"

'''Now we will create a header, this is all wrapped in a variable'''
'''we will use f strings to execute teh variables in-line in the message'''
'''and use """ """ to create a multi-line string'''
message = f"""From: Danish Kode Monkey{sender} 
To: Myself {receiver}
Subject:{subject}\n
{body}
"""

#Now we create a server object called server using the SMTP library

server = smtplib.SMTP("smtp.gmail.com",587) #Create server object using smtplib.SMTP function, with arguments "smtp.gmail.com" (gmails smtp service) and a port, 587, the default mail transfer port.
server.starttls() #start server transport layer security

#now to log in to the server using our sender and password variables
server.login(sender,password)
print("Logged in...") #Just a simple print of success
server.sendmail(sender, receiver, message)
print("Email has been sent!")

#I stopped here because I realised its pretty unsafe, I will experiment more with mails in python
#if it ever becomes relative