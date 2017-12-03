# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 18:47:45 2017

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
a =  float(0) # lower bound of Integration
b = float(100) # upper bound of Integration
N = float(10) # number of segments
h = b - a # length of interval
dt = .1 #h/N <-- use this if you want to specify in terms of number of divisions
tList = np.arange(a,b+dt,dt) # list of values of t spaced by dt
r = 0.1 #coeffecient for how fast coffee cools
T_s = 17 #surrounding temperature
T_0 = 90. #Initial Temperature

def function(t): # defines function that takes time in analytic function
  return float(T_s-(T_s-T_0)*np.exp(-r*t)) # returns arguemnt through function

def functionDerivitive(y,t): # defines function that is equal to the value of the DE
  return float(-r*(y-T_s))
  
def AnalyticFunction(): #makes list straight from function
    l = [] # makes an empty list
    for i in tList: #runs each element of b through loop seperately
        l.append(float(function(i))) #adds function(i) to the list l as an integer
    return l # returns newly made function l

def SimpleEulerMethod(): #simple Euler method with c as initial condition for the start of list
  l = [] # makes empty list
  yi = function(a) # initial condition is set to boundary condition through function
  for i in tList: #makes y values fo the corresponding t values
    l.append(yi) #add new yi to list l
    yi += dt*functionDerivitive(yi,i)
  return l

def ImprovedEulerMethod(): #simple Euler method with c as initial condition for the start of list
  l = [] # makes empty list
  yi = function(a) # initial condition is set to boundary condition through function
  for i in tList: #makes y values fo the corresponding t values
    l.append(yi) #add new yi to list l
    yi += dt*(0.5)*(functionDerivitive(yi,i)+functionDerivitive(yi+dt*functionDerivitive(yi,i),i+dt))
  return l


plt.plot(tList, AnalyticFunction(),color="blue", linewidth=5, linestyle="--", label="Analytic")
plt.plot(tList,ImprovedEulerMethod(),color="red", linewidth=3, linestyle="-", label="Improved Euler Method")
plt.plot(tList,SimpleEulerMethod(),color="green", linewidth=1, linestyle="-", label="Simple Euler Method")
plt.xlabel('Time (mins)')
plt.ylabel('Temperature (C)')
plt.grid(True)
plt.plot([a, b], [T_s, T_s], color='k', linestyle='-', linewidth=2, label = "Surroundings Temperature")
plt.legend(loc='upper right', frameon=True, prop={'size': 15})
plt.savefig('graph.png')