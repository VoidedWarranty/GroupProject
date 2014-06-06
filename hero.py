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
class hero:
    def __init__(self,health, maxhealth, item, x, y,limitX,limitY,mattack):
        """ Constructs a hero from the given args. """
        global mx,my,mhealth,mmhealth,mitem,potions,f,g, attack
        mx = x
        my = y
        mhealth = health
        mmhealth = maxhealth
        mitem = item
        potions=5
        f=limitX
        g=limitY
        attack = mattack
        
    def getX(self):
        """ Returns X."""
        return mx

    def getY(self):
        """ Returns Y."""
        return my
    def getItem(self):
        """ Returns the item in the item slot.  """
        return mitem
    def getHealth(self):
        """ Returns the hero's health. """
        return mhealth
    def getMaxHealth(self):
        """ Returns the hero's maximum health. """
        return mmhealth
    def moveUp(self):
        """ Moves the hero one tile upwards, or until the top of the screen. """
        global my
        if my>=40 :
            my-=40
    def moveDown(self):
        """ Moves the hero one tile downwards, or until he reaches the bottom of the screen. """  
        global my,g
        if my<=40*(g-1):
            my+=40
    def moveLeft(self):
        """ Moves the hero one tile left, or until he reaches the left wall of the screen. """  
        global mx
        if mx>=40:
            mx-=40
    def moveRight(self):
        """ Moves the hero one tile right, or until he reaches the right wall of the screen. """  
        global mx,f
        if mx<=40*(f-1):
            mx+=40
    def setItem(self,item):
        """ Chooses the item in the item slot. """
        global mitem
        mitem = item
    def setHealth(self,health):
        """Decides the hero's health. """
        global mhealth
        if (self.getHealth()<self.getMaxHealth()):
            mhealth=health
        else:
            mhealth = self.getMaxHealth()
    def setMaxHealth(self,mhealth):
        """ Set's the hero's max health. """
        global mmhealth
        mmhealth= mhealth
    def setAttack(self, nAttack):
            """ Set's the hero's attack."""
        global attack
        attack = nAttack
    def getAttack(self):
        """Returns the hero's attack."""
        global attack
        return attack
    def getLevel(self):
        """Returns the hero's level. """
        global level
        return level
    def setLevel(self, slevel):
        """Sets the hero's level. """
        global level
        level = slevel
        self.setAttack(self.getAttack())
        self.setMaxHealth(self.getMaxHealth())
    def healSelf(self,heal):
        """ heals the player by the specified amount, or to their max health, whichever comes first. """
        global mhealth,health
        health+=heal
        if health>mhealth:
            health=mhealth
    def healthPotion(self): 
        """Uses one health potion, if available. Heals for 10 health currently. """
        global potions
        if potions>0:
            healSelf(self,10)
            potions-=1
