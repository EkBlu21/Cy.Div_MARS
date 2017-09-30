#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 20:53:21 2017

@author: ek_blu
"""
import Tkinter as tkr
import tkMessageBox

#####DEFINE MAIN WINDOW
root = tkr.Tk()
root.title("Cyber|Divison Management Analytics & Records System")
root.minsize(width= 550, height = 350)
root.maxsize(width= 1200, height = 700)
#root["bg"] = "#710000"
root["bg"] = "#660033"

##### MAIN LAYOUT FRAMES
frame = tkr.Frame(root)
frame.pack(pady=35)
#frame["bg"] = "darkslategray"
btmframe = tkr.Frame(root)
btmframe.pack(pady=15, side = 'bottom')
#btmframe["bg"] = "#003e12"

rgtframe = tkr.Frame(root)
rgtframe.pack(side = 'right')

lftframe = tkr.Frame(root)
lftframe.pack(side = 'left')


##### BUTTONS/FUNCTIONS
def addRecord():
     tkMessageBox.showinfo( 'Records', 'Add To Records API Here')
     
button0 = tkr.Button(btmframe, fg="blue", text = "Add Record", command = addRecord)
button0.pack(side = 'left', padx = 10, pady=5, ipadx=10)
button0["bg"] = "coral"

def addAppointment():
     tkMessageBox.showinfo( 'Calendar', 'Add To Calendar API Here')
     
button1 = tkr.Button(btmframe, fg="blue", text = "Calendar", command = addAppointment)
button1.pack(side = 'left', padx = 10, pady=5, ipadx=10)
button1["bg"] = "coral"

def addRequest():
     tkMessageBox.showinfo( 'Requsts', 'Add To Requests API Here')
     
button2 = tkr.Button(btmframe, fg="blue", text = "Send Request", command = addRequest)
button2.pack(side = 'left', padx = 10, pady=5, ipadx=10)
button2["bg"] = "coral"

##### Log_Into_BCC_MARS

username = "Erick"
userpswd = "Erick123"

id_label = tkr.Label(frame, text='Enter User ID:')
id_label.pack()
id_entry = tkr.Entry(frame)
id_entry.pack( pady= 5, padx=2)

pswd_label = tkr.Label(frame, text='Enter Password:')
pswd_label.pack()
pswd_entry = tkr.Entry(frame, show='*')
pswd_entry.pack( pady=5, padx=2)


def log_in():
    if username == id_entry.get() and userpswd == pswd_entry.get():
        tkMessageBox.showinfo("Welcome Erick", "Cy.Div MARS Credentials Confirmed\n\nYou Will Now Be Redirected To Your Homepage")
    else:
        tkMessageBox.askretrycancel("Invalid Log In Credentials", "We Could Not Verify Your ID & Password")
     
log_inbutton = tkr.Button(frame,fg="blue",bg="coral", text ="Log Into CyDiv.MARS", command = log_in).pack(pady=2)



     







root.mainloop()


