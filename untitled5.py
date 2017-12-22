# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 15:53:14 2017

@author: Cormac
"""

import numpy as np

t0=float(0)                                              #Start time (mins)
tf=float(40)                                              #End time (mins) either 5 or 40
T0=float(90)                                             #Initial Temperature of coffee
Ts=float(17)                                             #Temperature of surroundings
r=0.1                                                    #Cooling Constant

dt1 = 0.125

dt2= 0.0001

time_list1 = np.arange(t0,tf+(dt1),dt1)                                 #Creating my x-axis (time range from 0-100min in steps of 0.1min)

time_list2 = np.arange(t0,tf+(dt2),dt2)  

def f(y):                                                #Defining f(y) to be the differential equation(Newton's law of cooling)
    return float(-r*(y-Ts))
    
Temps1 = []                                           #Creates an empty list


def Eul1():                                           #Implementing the Improved Euler method
    y = T0  	                                        #Defining initial temperature value = y
    for i in time_list1:                                          #For every value in list t (continued on next line)
        Temps1.append(y)                                  #add y to the list "Temps"
        y += (f(y)+f(y+f(y)*dt1))*(dt1/2)                  #Improved Euler method that makes temperature values (y values) to add to "Temps                                        
    #print "T1=", Temps1                                        #Prints the list of temperature values
    return Temps1                                        #terminates the execution of the function and returns control to the calling function  
Eul1()    

Temps2 = []

def Eul2():                                           #Implementing the Improved Euler method
    y = T0  	                                        #Defining initial temperature value = y
    for j in time_list2:                                          #For every value in list t (continued on next line)
        Temps2.append(y)                                  #add y to the list "Temps"
        y += (f(y)+f(y+f(y)*dt2))*(dt2/2)                  #Improved Euler method that makes temperature values (y values) to add to "Temps
    #print "T2=", Temps2                                         #Prints the list of temperature values
    return Temps2 
Eul2()

def An(t):                                               #Defines a function An(t) that will generate temperatures for every t value in the range defined above. This function is defined according to the solution of the differential equation known as Newton's cooling law
     return (Ts)-((Ts-T0)*np.exp(-r*t))
     
endtime_an = An(40) 
endtime_Eul1 = Temps1[-1]          #Defines The "End time" for the Improved Euler method as the temperature at t=10min
endtime_Eul2 = Temps2[-1]               #Defines The "End time" for the Analytical solution as the temperature at t=10min
print "% accuracy =", abs(100-((endtime_Eul1/endtime_Eul2)*100))
print "Temp@ 5min Eul1 =" ,endtime_Eul1                #Prints The "End time" for the Improved Euler method 
print "Temp@ 5min Eul2 =" ,endtime_Eul2