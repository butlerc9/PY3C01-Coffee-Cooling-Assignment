# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 20:33:48 2017

@author: Cormac
"""


import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib as mpl
import random

"""Constant Initialisation"""
    
n = int(6) #size of matrix
temperature = 3. #temperature

x, y = np.mgrid[0:n,0:n] #creates a nxn matrix

"""Function Definitions"""



def RandomMatrix(n): # Initialize spins 0 and 1 by random. 
    return np.random.randint(2, size=(n,n))*2 -1

def FigurePlotter():
    fig = plt.figure()
    ani = animation.FuncAnimation(fig, SpinChange, frames=19, interval=20)
    plt.title("Temperature="+str(temperature))
    plt.xlabel('X')
    plt.ylabel('Y')

spins = RandomMatrix(n)

def SpinChange(i):
    x = random.randint(0,n)
    y = random.randint(0,n)
    spins[x,y] *= -1
    return spins


FigurePlotter()






plt.show()
plt.show()