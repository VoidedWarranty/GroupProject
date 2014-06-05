#File: interface.py
#description: this file creates the user interface that shows items, health, etc. and updates it.
from Tkinter import * # <---- all imports used for main
from multiprocessing import Process
import ImageTk
import ctypes
import Image
import sys
import winsound
from items import *
from mob import *
from interface import *
from fileSave import *
from Sound import *
from random import randint

def createInterface(f,r,w,h,health,mhealth):
    #var = StringVar()
    #label = Label(root, textvariable=var, relief=RAISED)
    bar = "health " + str(health) + "/" + str(mhealth)
    #r.delete(f)
    print bar
    r.itemconfig(f, text=bar)
    #bob.set(w,h, text = bar, fill = "red", font = ('Times', 20, 'bold'), anchor = 'nw')
