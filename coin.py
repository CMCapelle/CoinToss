#Coin class for coin toss program

import random 

class Coin:
     
    #The _ _init_ _ method initializes the sideup data attribute with 'Tails' and amount to 20.
    def __init__(self, amount = 20, sideup = 'Heads'):
        self._amount = amount
        self._sideup = sideup

    def get_amount(self):
        return self._amount

    def set_amount(self, x):
        self._amount += x
     
    #generates a random number 1 and 0 using randint function.
    def toss(self):

        if random.randint(0,1) == 0:
            self.sideup  = 'Tails'
        else:
            self.sideup  = 'Heads'
     
    #returns the value referenced by sideup.
    def get_sideup(self):
        return self.sideup

