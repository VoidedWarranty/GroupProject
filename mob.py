#File: mob.py
#description: this file creates the different types of mobs and spawns them in each room"

from random import *

def mobSpawn(): #spawns a random amount of mobs for each floor
    i = randint(1,6)
    for x in range(i):
        print "mob " + str(x) + " has been spawned"
        
