from Tkinter import Tk, Frame, Canvas
import ImageTk
import ctypes
import Image
import sys
from items import *
from mob import *


def quitApp(event):
    root.destroy()

def moveUp(event):
    print "moveUp method works"
    
def moveDown(event):
    print "moveDown method works"
    
def moveLeft(event):
    print "moveLeft method works"
    
def moveRight(event):
    print "moveRight method works"

def useItem(event):
    itemUse(None)
    print "useItem Method works"
def mainSpawn():
    mainChar = ImageTk.PhotoImage(Image.open("Karel.jpg"))
    canvas.create_image(40,40, image=mainChar)
    print "main character has been called"

    
user32 = ctypes.windll.user32
w = int(user32.GetSystemMetrics(0))
h = int(user32.GetSystemMetrics(1))
f = int(w/40)
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
root.bind("<Escape>", quitApp) # kills program
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
mainSpawn()
mobSpawn()
frame.pack()
root.mainloop()
