# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 18:24:00 2016
T=1000ms  
@author: XAXA

"""
import pylab
from pylab import pi,sin
import time as t
import u3
d = u3.U3()
d.configU3()

DAC0 = 5000
T=input("Zadejte dobu trvana funkce v sekundách: ")
a=input("Zadejte Umax(0-5): ")
f=input("Zadejte frekvenci: ")
a=a/2
print "/nspuštím ..."
d.writeRegister(DAC0,a)
t.sleep(0.8)
cas= t.clock()
print "/nstart"
while T>t.clock():
    u=a*sin(f*2*pi*(t.clock()-cas))+a
    d.writeRegister(DAC0,u)
    print d.readRegister(0), t.clock()
d.close()






