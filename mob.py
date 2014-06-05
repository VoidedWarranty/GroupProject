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
from Move import *
from random import *

def mobSpawn(): #spawns a random amount of mobs for each floor
    i = randint(1,6)
    for x in range(i):
        print "mob " + str(x) + " has been spawned"
        

class mob:
    def __init__(self,health, maxhealth, item, x, y):
        global mx,my,mhealth,mmhealth,mitem
        mx = x
        my = y
        mhealth = health
        mmhealth = maxhealth
        mitem = item
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
    def getAttack(self, nAttack):
        global attack
        attack = nAttack
    def attack(self, heroHealth):
        hero.setHealth(hero.getHealth() - (self.getAttack() + randint(-(self.getAttack()/10), self.getAttack()/10))
    def pathfind(self, hero.getX(), hero.getY()):
        listMoves = [(((hero.getY-self.getY-40)**2+(hero.getX-self.getX)**2)**.5), (((hero.getY-self.getY+40)**2+(hero.getX-self.getX)**2)**.5), (((hero.getY-self.getY)**2+(hero.getX-self.getX-40)**2)**.5), (((hero.getY-self.getY)**2+(hero.getX-self.getX+40)**2)**.5)]
        m=0
        mi=0
        for i in range(len(myList)):
            if m<listMoves[i]:
                m=myList[i]
                mi=i
        if (mi == 0):
            self.moveUp()
        else if (mi == 1):
            self.moveDown()
        else if (mi == 2):
            self.moveLeft()
        else:
            self.moveRight()
<<<<<<< HEAD




        
=======
>>>>>>> 5ee138f80b8fd3f1a295caede3869a3325f0dc37
