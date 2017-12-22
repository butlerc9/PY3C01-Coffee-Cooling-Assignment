# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:19:44 2017

@author: Cormac
"""

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib as mpl
import random

fig = plt.figure()


def f(x, y):
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

im = plt.imshow(f(x, y), animated=True,cmap = 'cool',interpolation = 'bilinear')
print f(x,y)
yes = f(x,y)


def updatefig(*args):
    global x, y
    x += np.pi / 50.
    y += np.pi / 20.
    im.set_array(f(x, y))
    print y
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)

plt.show()