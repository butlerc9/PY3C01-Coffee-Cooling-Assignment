# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 22:50:37 2017

@author: Cormac
"""

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib as mpl
import random

"""Constant Initialisation"""
    
n = int(10) #size of square matrix
temperature = 3. #temperature




""" Random Matrix Generation """
def RandomMatrix(n): #Generates Random n x n Matrix  
    return np.random.randint(2, size=(n,n))*2 -1 #Generates Matrix Full of random 0,2s and then subtracts 1 to get +-1 matrix

Lattice = RandomMatrix(n) #Initialises Lattice as a random n x n matrix

"""Spin Changing Function"""

def SpinChange(i): #flips spin of random paticle. i is dummy variable 
    x = random.randint(0,n-1) #random x value
    y = random.randint(0,n-1) #random y value
    Lattice[x,y] *= -1 #flips random x,y coordinate
    matrice.set_array(Lattice) #updates Lattice array to new configuration




fig, ax = plt.subplots()
matrice = ax.matshow(Lattice)

ani = animation.FuncAnimation(fig, SpinChange, frames=19, interval=0.1)
plt.show()