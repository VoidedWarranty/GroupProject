#File: items.py
#description: this supplies methods to check for what item you have in hand and uses it
def itemUse(event):
    if hasItem():
        print "Character has item and method works"

def hasItem():
    print "hasItem method works"
    return True

def items(): #this is a main method that would create weapons and potions for the person to use
    print "items are created"
    
