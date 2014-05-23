#Names: Ian Carr, Samuel Kebadu, Jerius Samra
#File: _init_.py
#Description: this is thhe main file that is initialized. You start the Program here


from Tkinter import Tk, Frame, Canvas # <---- all imports used for main
import ImageTk
import ctypes
import Image
import sys
from items import *
from mob import *
from interface import *
from fileSave import *

def quitApp(event): #<---- how to quit the app and save
    save()
    root.destroy()

def moveUp(event): #hero's movement: up
    print "moveUp method works"
    
def moveDown(event):#hero's movement: down
    print "moveDown method works"
    
def moveLeft(event):#hero's movement: left
    print "moveLeft method works"
    
def moveRight(event):#hero's movement: right
    print "moveRight method works"

def useItem(event): #use an item in your hand
    itemUse(None)
    print "useItem Method works"
    
def mainSpawn(): #spawns main character
    mainChar = ImageTk.PhotoImage(Image.open("Karel.jpg"))
    canvas.create_image(40,40, image=mainChar)
    print "main character has been called"


    
user32 = ctypes.windll.user32 #renders size to fullscreen
w = int(user32.GetSystemMetrics(0))
h = int(user32.GetSystemMetrics(1))
f = int(w/40) # calculates how many tiles needed
g = int(h/40)

print w

root = Tk()
root.title("Transparency")
frame = Frame(root)
canvas = Canvas(frame, bg="black", width=w, height=h)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
print w, h
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", quitApp) # All root bindings
root.bind("w", moveUp) 
root.bind("s", moveDown)
root.bind("a", moveLeft)
root.bind("d", moveRight)
root.bind("<Button-1>",useItem)
canvas.pack()





photoimage = ImageTk.PhotoImage(Image.open("dungeonTile.jpg"))
#im = Image.open("Karel.png")
#print im.mode
x = 0
y = 0
#for i in range(f+1):
#    for k in range(g+1):
#        canvas.create_image(i*40, k*40, image=photoimage)
mainSpawn() #spawns main
mobSpawn()  #spawns mobs
createInterface() #creates user interface
frame.pack()
root.mainloop()
