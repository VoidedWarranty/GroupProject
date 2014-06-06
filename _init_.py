#Names: Ian Carr, Samuel Kebadu, Jerius Samra
#File: _init_.py
#Description: this is the main file that is initialized. You start the Program here
from Tkinter import Tk, Frame, Canvas # <---- all imports used for main
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
from hero import *
global bill
index = 0
bill = 0

def quitApp(event):#<---- how to quit the app and save
    global root, p, q
    print "stopping..."
    #p.terminate()
    save()
    root.destroy()

def moveUp(event): #hero's movement: up
    global MainChar, x, y, canvas, bob, enemy
    Link.moveUp()
    actMove(numMob(),canvas, Link, enemy)
    bar = "health " + str(Link.getHealth()) + "/" + str(Link.getMaxHealth())
    canvas.itemconfig(bob, text=bar)
    canvas.coords(MainChar,Link.getX(),Link.getY())
    root.update()
    
def moveDown(event):#hero's movement: down
    global MainChar, x, y, canvas, bob, enemy
    Link.moveDown()
    actMove(numMob(),canvas, Link, enemy)
    bar = "health " + str(Link.getHealth()) + "/" + str(Link.getMaxHealth())
    canvas.itemconfig(bob, text=bar)
    canvas.coords(MainChar,Link.getX(),Link.getY())
    root.update()    
def moveLeft(event):#hero's movement: left
    global MainChar, x, y, canvas, bob, enemy
    Link.moveLeft()
    actMove(numMob(),canvas, Link, enemy)
    bar = "health " + str(Link.getHealth()) + "/" + str(Link.getMaxHealth())
    canvas.itemconfig(bob, text=bar)
    canvas.coords(MainChar,Link.getX(),Link.getY())
    root.update()    
def moveRight(event):#hero's movement: right
    global MainChar, x, y, canvas, Link, bob, enemy
    Link.moveRight()
    actMove(numMob(),canvas, Link, enemy)
    bar = "health " + str(Link.getHealth()) + "/" + str(Link.getMaxHealth())
    canvas.itemconfig(bob, text=bar)
    canvas.coords(MainChar,Link.getX(),Link.getY())
    root.update()
def useItem(event): #use an item in your hand
    global Link, enemy
    attackMob(Link)
    actMove(numMob(),canvas, Link, enemy)
    bar = "health " + str(Link.getHealth()) + "/" + str(Link.getMaxHealth())
    canvas.itemconfig(bob, text=bar)
    print "useItem Method works"
    root.update()
    
def mainSpawn(): #spawns main characte
    global MainChar, x, y, canvas, mainChar, Link,f,g
    x = 400
    y = 400
    Link = hero(30,30,None,x,y,f,g,20)
    #mainChar = ImageTk.PhotoImage(Image.open("Karel.jpg"))
    MainChar = canvas.create_image(x,y, image=mainChar, tag='MainC')
    #print "main character has been called"

global MainC
def music():
    winsound.PlaySound('Naruto-Breakdown.wav', winsound.SND_FILENAME)

def start():
    global canvas, mainChar, root, i, k, bob, Link, bill, f, g, enemy
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
    #root.bind("h", healthPotion)
    root.bind("<space>", useItem)

    canvas.pack()




    photoimage = ImageTk.PhotoImage(Image.open("dungeonTile.jpg"))
    mainChar = ImageTk.PhotoImage(Image.open("CobaltKnight.png"))
    enemy = ImageTk.PhotoImage(Image.open("LobsterRoach.png"))
    im = Image.open("Karel.png")
    print im.mode
    x = 0
    y = 0
    print bill, "bill"
    if bill == 0:
        for i in range(f+1):
            for k in range(g+1):
                canvas.create_image(i*40, k*40, image=photoimage)
        bill = 1
    mainSpawn() #spawns main
    mobSpawn(canvas,enemy)  #spawns mobs
    #bob = Label(canvas,width=w,height=h, text = "health", fg = 'red', font = ('Times', 30, 'bold'), anchor = 'nw')
    #bob.pack()
    bob = canvas.create_text(40,40, text = "bob", fill = "red", font = ('Times', 30, 'bold'), anchor = 'nw')
    bar = "health " + str(Link.getHealth()) + "/" + str(Link.getMaxHealth())
    canvas.itemconfig(bob, text=bar)
    canvas.create_rectangle(w-120, 40 , w-40, 120, fill='black', outline = 'white')
    canvas.create_rectangle(w-240, 40 , w-160, 120, fill='black', outline = 'white')
    #createInterface(bob,canvas,i,k,Link.getHealth(),Link.getMaxHealth()) #creates user interface
    #bob.pack()
    frame.pack()
    print "music"
    #canvas.create_text(i,k, text = "health", fill = 'red', font = ('Times', 30, 'bold'), anchor = 'nw')

    #f= wave.open( 'Naruto-Breakdown.wav', 'rb' )
    #sampleRate= f.getframerate()
    #channels= f.getnchannels()
    #format = sound.AFMT_S16_LE
    #snd= sound.Output( sampleRate, channels, format )
    #s= f.readframes( 300000 )
    #snd.play( s )
    #while snd.isPlaying(): time.sleep( 0.05 )
    #canvas.pack()
    root.mainloop()
if __name__ == '__main__':
    global p, q
    start()
    #p = Process(target=music)
    #p.start()



