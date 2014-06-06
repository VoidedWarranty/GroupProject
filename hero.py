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
    def __init__(self,health, maxhealth, item, x, y):
        global mx,my,mhealth,mmhealth,mitem,potions
        mx = x
        my = y
        mhealth = health
        mmhealth = maxhealth
        mitem = item
        potions=5
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
    def heal(self,heal):#heals the player by the specified amount, or to their max health, whichever comes first.
        global mhealth,health
        health+=heal
        if health>mhealth:
            health=mhealth
    def healthPotion(self): #Uses one health potion, if available.  Heals for 7 health currently.
        global potions
        if potions>0:
            heal(self,10)
            potions-=1
