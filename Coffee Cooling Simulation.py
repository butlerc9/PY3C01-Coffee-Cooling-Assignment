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
b = float(10) # upper bound of Integration
dt = .001 #h/N <-- use this if you want to specify in terms of number of divisions
h = a-b
N = h/dt
tList = np.arange(a,b+dt,dt) # list of values of t spaced by dt
r = 0.1 #coeffecient for how fast coffee cools
T_s = 17 #surrounding temperature
T_0 = 90. #Initial Temperature
dt_range1 = np.arange(0.0001,0.1,0.0001)
dt_range = np.logspace(0.0001,0.1,1000)
dt_values = [0.1,0.05,0.025,0.01,0.005,0.0025,0.001] #range of dt values for finding error


def function(t): # defines function that takes time in analytic function
  return float(T_s-(T_s-T_0)*np.exp(-r*t)) # returns arguemnt through function

def functionDerivitive(y,t): # defines function that is equal to the value of the DE
  return float(-r*(y-T_s))
  
def AnalyticFunction(): #makes list straight from function
    l = [] # makes an empty list
    for i in tList: #runs each element of b through loop seperately
        l.append(float(function(i))) #adds function(i) to the list l as an integer
    return l # returns newly made function l

def SimpleEulerMethod(dt): #simple Euler method with c as initial condition for the start of list
  l = [] # makes empty list
  yi = function(a) # initial condition is set to boundary condition through function
  tList = np.arange(a,b+dt,dt)
  for i in tList: #makes y values fo the corresponding t values
    l.append(yi) #add new yi to list l
    yi += dt*functionDerivitive(yi,i)
  return l[-1]

def ImprovedEulerMethod(dt): #simple Euler method with c as initial condition for the start of list
  l = [] # makes empty list
  yi = function(a) # initial condition is set to boundary condition through function
  tList = np.arange(a,b+dt,dt)
  for i in tList: #makes y values fo the corresponding t values
    l.append(yi) #add new yi to list l
    yi += dt*(0.5)*(functionDerivitive(yi,i)+functionDerivitive(yi+dt*functionDerivitive(yi,i),i+dt))
  return l[-1]

true_analytic_value = AnalyticFunction()[-1]
ApproxValues = []
for i in dt_range1:
    ApproxValues.append(ImprovedEulerMethod(i))

plt.scatter(dt_range1,ApproxValues,marker='^',color='g')

ApproxValues = []
for i in dt_values:
    ApproxValues.append(ImprovedEulerMethod(i))

plt.scatter(dt_values,ApproxValues,marker='o',color='b',s=100)



plt.savefig('graph.png')