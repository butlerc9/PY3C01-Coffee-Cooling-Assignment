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
b = float(5) # upper bound of Integration
dt = .1 #specify step size
h = b-a #interval length
N = h/dt
tList = np.linspace(a,b,N+1) # list of values of t spaced by dt
r = .1 #coeffecient for how fast coffee cools
T_s = 17. #surrounding temperature
T_0 = 90. #Initial Temperature
dt_range = [0.1,0.05,0.025,0.01,0.005,0.001]#values of dt which he gives

"""Function Defining"""

def function(t): # defines function that takes time in analytic function
  return float(T_s-(T_s-T_0)*np.exp(-r*t)) # returns arguemnt through function

def functionDerivitive(y,t): # defines function that is equal to the value of the DE
  return float(-r*(y-T_s))
  
def AnalyticFunction(): #makes list straight from function
    l = [] # makes an empty list
    for i in tList: #runs each element of b through loop seperately
        l.append(float(function(i))) #adds function(i) to the list l as an integer
    return l # returns newly made function l

def SimpleEulerStep(yi,i,dt): 
    return dt*functionDerivitive(yi,i)

def ImprovedEulerStep(yi,i,dt):
    return dt*(0.5)*(functionDerivitive(yi,i)+functionDerivitive(yi+dt*functionDerivitive(yi,i),i+dt))

def RichardsonStep(yi,i,dt):
      y1 = yi + ImprovedEulerStep(yi,i,dt) #create a variable y1 which steps a distance of dt
      y21 = yi + ImprovedEulerStep(yi,i,dt/2) #creates variable y2 which will go in steps of dt/2 in two steps.
      y22 = y21 + ImprovedEulerStep(y21,i,dt/2) #the second number is to indicate the steps
      return ((4*y22)-y1)/3

def RichardsonStepError(yi,i,dt):
      y1 = yi + ImprovedEulerStep(yi,i,dt) #create a variable y1 which steps a distance of dt
      y21 = yi + ImprovedEulerStep(yi,i,dt/2) #creates variable y2 which will go in steps of dt/2 in two steps.
      y22 = y21 + ImprovedEulerStep(y21,i,dt/2) #the second number is to indicate the steps
      return y1-y22

def ErrorNumericalStep(yi,i,dt):
    SimpleEulerStep(yi,i,dt)

def SimpleEulerMethod(dt): #simple Euler method with c as initial condition for the start of list
  l = [] # makes empty list
  yi = function(a) # initial condition is set to boundary condition through function
  N = h/dt
  tList = np.linspace(a,b,N+1) # list of values of t spaced by dt
  for i in tList: #makes y values fo the corresponding t values
    l.append(yi) #add new yi to list l
    yi += SimpleEulerStep(yi,i,dt)
  return l

def ImprovedEulerMethod(dt): #simple Euler method with c as initial condition for the start of list
  l = [] # makes empty list
  yi = function(a) # initial condition is set to boundary condition through function
  N = h/dt
  tList = np.linspace(a,b,N+1) # list of values of t spaced by dt
  for i in tList: #makes y values fo the corresponding t values
    l.append(yi) #add new yi to list l
    yi += ImprovedEulerStep(yi,i,dt)
  #plt.plot(tList,l,color="red", linewidth=3, linestyle="--", label="Improved Euler Method")
  return l

def RichardsonInterpolation(dt):
  l = [] # makes empty list
  yi = function(a) # initial condition is set to boundary condition through function
  N = h/dt
  tList = np.linspace(a,b,N+1) # list of values of t spaced by dt
  for i in tList:
      l.append(yi)
      yi = RichardsonStep(yi,i,dt)
  return l

def AdaptiveStepSizes():
    dt0 =.005 #initial step size
    yi = function(a) # initial condition is set to boundary condition through function
    i = a # initialises t as a value
    delta_t = dt0
    errormax = 0.0001
    l = [] # makes empty list
    t_values = [] #creates empty list for dt values. This will be specific to each iteration
    errors = []    #creates new array for error values
    while i < b: #until t value is greater than boundary set
        error = RichardsonStepError(yi,i,delta_t)
        if  0.99 < error/errormax < 1.01:
               yi = RichardsonStep(yi,i,delta_t) #new y value = old value + richardson step
               i += delta_t #new t value is updated
               l.append(yi) #update for y values of function
               t_values.append(i) #stores t values
               errors.append(error)
        else:
            delta_t *= (errormax/error)**(0.5)
            print "i,delta_t, (errormax/error)**(0.5)",i,delta_t, (errormax/error)**(0.5)
    plt.plot(t_values,errors)
    return l

def ErrorAnalytical(dt_list,function1):
  errors = []
  true_value = function(b)
  for i in dt_list:
      errors.append(100*(np.abs(function1(i)[-1]-true_value))/true_value) #plots % error in function given as argument
  return errors

def ErrorNumerical(dt_list):
    errors = []
    for i in dt_list:
        errors.append(100*(np.abs(ImprovedEulerMethod(i)[-1]-ImprovedEulerMethod(i/5)[-1]))/ImprovedEulerMethod(i/5)[-1])
    return errors


""" Plotting and Testing  """


plt.plot(dt_range,ErrorNumerical(dt_range), linewidth=2,label = 'Numerical Comparison dt/5',color="green")
plt.scatter(dt_range,ErrorNumerical(dt_range),s=70,color="green")

plt.plot(dt_range,ErrorAnalytical(dt_range,RichardsonInterpolation), linewidth=2,label = 'Richardson Interpolation',color="red")
plt.scatter(dt_range,ErrorAnalytical(dt_range,RichardsonInterpolation),s=70,color="red")

plt.plot(dt_range,ErrorAnalytical(dt_range,ImprovedEulerMethod),linewidth=2,label = 'Improved Euler Method',color="blue", linestyle="--")
plt.scatter(dt_range,ErrorAnalytical(dt_range,ImprovedEulerMethod),s=70,color="blue")

plt.plot([dt_range[0], dt_range[-1]], [0,0], color='k', linestyle='--', linewidth=1, label = "zero error") #plots 0 error lines

#plt.plot(tList, RichardsonInterpolation(0.1),color="pink", linewidth=2, linestyle="-", label="Richardson")
#plt.plot(tList, AnalyticFunction(),color="blue", linewidth=1, linestyle="-", label="Analytic")
#plt.plot(tList,ImprovedEulerMethod(0.1),color="red", linewidth=1, linestyle="--", label="Improved Euler Method")
#plt.plot(tList,SimpleEulerMethod(0.1),color="green", linewidth=1, linestyle="-", label="Simple Euler Method")
plt.xlabel('Time Step (mins)')
plt.ylabel('Percentage Error (%)')
plt.grid(True)
#plt.plot([a, b], [T_s, T_s], color='k', linestyle='-', linewidth=2, label = "Surroundings Temperature")
plt.legend(loc='lower right', frameon=True, prop={'size': 15})


plt.show()