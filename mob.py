#File: mob.py
#description: this file creates the different types of mobs and spawns them in each room"
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
from random import *
from _init_ import *
global i, d, f
d = None
i = None
f = None
def actMove(num, r, l, pic):
    """Performs an action and ticks the timer."""
    global root
    actions = 0 
    for x in range(num):
        if (d["mob" + str(x)].getAlive() == True):
            d["mob" + str(x)].interact(l.getX(), l.getY(), l)
            r.coords(f["pic" + str(x)],d["mob" + str(x)].getX(),d["mob" + str(x)].getY())
            print d["mob" + str(x)].getAlive()
            actions +=1
            l.setHealth(l.getHealth() + 3)
        else:
            r.delete(f["pic" + str(x)])
    if (actions == 0):
        mobSpawn(r, pic)
        l.setMaxHealth(l.getMaxHealth() + 20)
        l.setHealth(l.getHealth()+20)
        l.setAttack(l.getAttack() + 5)
        #l.setLevel(l.getLevel()+1)
        #l.setMaxHealth(l.getMaxHealth())
        #l.setAttack(l.getAttack())
        
    if (l.getHealth()<=0):
        r.delete('all')
    print "done"
def mobSpawn(r,inn):
    """Spawns a random amount of mobs for each floor.  """
    global i, d, f
    i = randint(1,6)
    d={}
    f={}
    for x in range(i):
            d["mob{0}".format(x)]= mob(10,10,2,None,200-(x*40),400)
            f["pic{0}".format(x)]= r.create_image(d["mob"+str(x)].getX(),d["mob"+str(x)].getY(), image=inn)
            print "derp"
def attackMob(l):
   """Attacks a given mob.  """
    global d, f
    for x in range(numMob()):
        if d["mob" + str(x)].getX() == l.getX() and d["mob" + str(x)].getY() == l.getY():
            d["mob" + str(x)].setHealth(d["mob" + str(x)].getHealth()-l.getAttack())
            d["mob" + str(x)].getAlive()
        
        

def numMob():
    """ Returns the number of mobs active on the map. """
    global i
    return i
        
        

class mob:
    def __init__(self,health, maxhealth, mattack, item, x, y):
        """ Constructs a mob, given these args. """
        global mx,my,mhealth,mmhealth,mitem, attack, alive
        mx = x
        my = y
        mhealth = health
        mmhealth = maxhealth
        mitem = item
        attack = mattack
        alive = True
    def getX(self):
        """ Returns the X coord of the mob. """
        return mx
    def getY(self):
        """ Returns the Y coord of the mob. """
        return my
    def getItem(self):
        """ Returns the item in the item slot. """
        return mitem
    def getAlive(self):
        """ Checks if still alive and returns resulting finding. """
        global alive
        if (self.getHealth()<=0):
            alive = False
        return alive
    def getHealth(self):
        """ Returns the health of the mob. """
        return mhealth
    def getMaxHealth(self):
        """ Returns the max health of the mob. """
        return mmhealth
    def moveUp(self):
        """ Moves the mob one tile up. """
        global my
        my-=40
    def moveDown(self):
        """ Moves the mob one tile down. """
        global my
        my+=40
    def moveLeft(self):
        """ Moves the mob one tile to the left. """
        global mx
        mx-=40
    def moveRight(self):
        """ Moves the mob one tile to the right. """
        global mx
        mx+=40
    def setItem(self,item):
        """ Sets the item in the item slot. """
        global mitem
        mitem = item
    def setHealth(self,health):
        """Sets the health of the mob. """
        global mhealth
        mhealth=health
    def setMaxHealth(self,mhealth):
        """ Sets the max health of the mob. """
        global mmhealth
        mmhealth= mhealth
    def setAttack(self, nAttack):
        """ Sets the attack of the mob. """
        global attack
        attack = nAttack
    def getAttack(self):
        """ Returns the attack of the mob. """
        return attack
    
    def attack(self, heroHealth, r):
        """ Attacks the hero. """
        r.setHealth(heroHealth - (self.getAttack() + randint(-(self.getAttack()/10), self.getAttack()/10)))
        print heroHealth - (self.getAttack() + randint(-(self.getAttack()/10), self.getAttack()/10))
    def pathfind(self, x, y):
        """ Locates the route between the mob's current position and the Hero's position. """
        listMoves = [(((y-self.getY()-40)**2+(x-self.getX())**2)**.5), (((y-self.getY()+40)**2+(x-self.getX())**2)**.5), (((y-self.getY())**2+(x-self.getX()-40)**2)**.5), (((y-self.getY())**2+(x-self.getX()+40)**2)**.5)]
        m=0
        mi=0
        for i in range(len(listMoves)):
            if m<listMoves[i]:
                m=listMoves[i]
                mi=i
        if (mi == 0):
            self.moveUp()
        elif (mi == 1):
            self.moveDown()
        elif (mi == 2):
            self.moveLeft()
        else:
            self.moveRight()
    def interact(self, x, y, hero):
        """ Performs the specified iteraaction. """
        if ((((y-self.getY())**2+(x-self.getX())**2)**.5) < 2.0):
            self.attack(hero.getHealth(), hero)
        else:
            self.pathfind(x,y)
        
