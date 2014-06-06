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
global i, d, f
d = None
i = None
f = None
def actMove(num, r, l):
    for x in range(num):
        d["mob" + str(x)].interact(l.getX(), l.getY(), l)
        r.coords(f["pic" + str(x)],d["mob" + str(x)].getX(),d["mob" + str(x)].getY())
        print "derp2"
        heal(self,3)
        
    print "done"
def mobSpawn(r,inn): #spawns a random amount of mobs for each floor\
    global i, d, f
    i = randint(1,6)
    d={}
    f={}
    for x in range(i):
            d["mob{0}".format(x)]= mob(10,10,2,None,200-(x*40),400)
            f["pic{0}".format(x)]= r.create_image(d["mob"+str(x)].getX(),d["mob"+str(x)].getY(), image=inn)
            print "derp"

def numMob():
    global i
    return i
        
        

class mob:
    def __init__(self,health, maxhealth, mattack, item, x, y):
        global mx,my,mhealth,mmhealth,mitem, attack
        mx = x
        my = y
        mhealth = health
        mmhealth = maxhealth
        mitem = item
        attack = mattack
    def getX(self):
        return mx
    def getY(self):
        return my
    def getItem(self):
        return mitem
    def getHealth(self):
        return mhealth
    def getMaxHealth(self):
        return mmhealth
    def moveUp(self):
        global my
        my-=40
    def moveDown(self):
        global my
        my+=40
    def moveLeft(self):
        global mx
        mx-=40
    def moveRight(self):
        global mx
        mx+=40
    def setItem(self,item):
        global mitem
        mitem = item
    def setHealth(self,health):
        global mhealth
        mhealth=health
    def setMaxHealth(self,mhealth):
        global mmhealth
        mmhealth= mhealth
    def setAttack(self, nAttack):
        global attack
        attack = nAttack
    def getAttack(self):
        return attack
    def attack(self, heroHealth, r):
        r.setHealth(heroHealth - (self.getAttack() + randint(-(self.getAttack()/10), self.getAttack()/10)))
    def pathfind(self, x, y):
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
        if ((((y-self.getY())**2+(x-self.getX())**2)**.5) < 2.0):
            self.attack(hero.getHealth(), hero)
        else:
            self.pathfind(x,y)
        
