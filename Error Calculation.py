 # -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 09:35:14 2017

@author: butlerc9
"""

"""
Created on Sun Dec 03 18:47:45 2017
@author: Cormac
"""

#Author: Cormac Butler
#Importing Packages
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# Numerical Integration Program using the Euler Methods
# First Euler Method uses rectangles to approximate the interval. Function is a function of y

"""Constants Setting"""
a =  float(0) # lower bound of Integration
b = float(10) # upper bound of Integration
dt = 0.1 #specify step size
h = b-a #interval length
N = h/dt
tList = np.linspace(a,b,N+1) # list of values of t spaced by dt
r = 0.1 #coeffecient for how fast coffee cools
T_s = 17. #surrounding temperature
T_0 = 90. #Initial Temperature
dt_range = [0.1,0.05,0.025,0.01,0.005,0.001]#values of dt which he gives

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
  N = h/dt
  tList = np.linspace(a,b,N+1) # list of values of t spaced by dt
  for i in tList: #makes y values fo the corresponding t values
    l.append(yi) #add new yi to list l
    yi += dt*functionDerivitive(yi,i)
  return l

def ImprovedEulerMethod(dt): #simple Euler method with c as initial condition for the start of list
  l = [] # makes empty list
  yi = function(a) # initial condition is set to boundary condition through function
  N = h/dt
  tList = np.linspace(a,b,N+1) # list of values of t spaced by dt
  print h,N,dt
  for i in tList: #makes y values fo the corresponding t values
    l.append(yi) #add new yi to list l
    yi += dt*(0.5)*(functionDerivitive(yi,i)+functionDerivitive(yi+dt*functionDerivitive(yi,i),i+dt))
  return l[-1]

true_value = function(10)

def ErrorCalculation():
    errors = []
    for i in dt_range:
        errors.append(100*(true_value-ImprovedEulerMethod(i))/true_value)
    return errors


plt.scatter(dt_range,ErrorCalculation(),label = 'time steps')
plt.plot(dt_range,ErrorCalculation())
plt.ylim(-0.0015,0.0005)
plt.ylabel('Time Step')
plt.xlabel('Percentage Error')
plt.plot([a, 0.1], [0, 0], color='k', linestyle='-', linewidth=2, label = "Zero Error")
plt.legend(loc='lower left', frameon=True, prop={'size': 15})
plt.show()



"""
plt.plot(tList, AnalyticFunction(),color="blue", linewidth=5, linestyle="--", label="Analytic")
plt.plot(tList,ImprovedEulerMethod(0.1),color="red", linewidth=3, linestyle="-", label="Improved Euler Method")
plt.plot(tList,SimpleEulerMethod(),color="green", linewidth=1, linestyle="-", label="Simple Euler Method")
plt.xlabel('Time (mins)')
plt.ylabel('Temperature (C)')
plt.grid(True)

plt.legend(loc='upper right', frameon=True, prop={'size': 15})
"""
#plt.savefig('graph.png')