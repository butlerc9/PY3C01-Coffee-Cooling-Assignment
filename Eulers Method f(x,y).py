# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 13:57:24 2017

@author: Cormac
"""

#Author: Cormac Butler
#Importing Packages
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


# Numerical Integration Program using the Euler Methods
# First Euler Method uses rectangles to approximate the interval. Function is a function of y

"""Constants Setting"""
a =  float(-9) # lower bound of Integration
b = float(9) # upper bound of Integration
N = float(100) # number of segments
h = b - a # length of interval
dt = float(h/N) # length of time step
tList = np.arange(a,b,dt) # list of values of t spaced by dt

def function(t): # defines function that squares argument
  return float(t**2) # returns arguemnt squared

def functionDerivitive(y,t): # defines function that doubles argument
  return float(t*2)
  
def AnalyticFunction(): #makes list straight from function
    l = [] # makes an empty list
    for i in tList: #runs each element of b through loop seperately
        l.append(float(function(i))) #adds function(i) to the list l as an integer
    return l # returns newly made function l

def ImprovedEulerMethod(): #simple Euler method with c as initial condition for the start of list
  l = [] # makes empty list
  yi = function(a) # initial condition is set to boundary condition through function
  for i in tList: #makes y values fo the corresponding t values
    l.append(yi) #add new yi to list l
    yi += dt*(0.5)*(functionDerivitive(yi,i)+functionDerivitive(yi+dt*functionDerivitive(yi,i),i+dt))
  return l

def SimpleEulerMethod(): #simple Euler method with c as initial condition for the start of list
  l = [] # makes empty list
  yi = function(a) # initial condition is set to boundary condition through function
  for i in tList: #makes y values fo the corresponding t values
    l.append(yi) #add new yi to list l
    yi += dt*functionDerivitive(yi,i)
  return l



plt.plot(tList, AnalyticFunction(),color="blue", linewidth=3, linestyle="-", label="Analytic")
plt.plot(tList,ImprovedEulerMethod(),color="red", linewidth=1, linestyle="-", label="Numerical Improved")
plt.plot(tList,SimpleEulerMethod(),color="green", linewidth=1, linestyle="-", label="Numerical Simple")
plt.show()