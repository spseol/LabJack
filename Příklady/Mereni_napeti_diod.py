# -*- coding: utf-8 -*-
"""
Created on Thu May 19 08:37:34 2016

@author: XAXA
"""
import time as t
import u3
d= None
d = u3.U3()
d.configU3()
R=227

d.writeRegister(5000,0)
t.sleep(0.5)

def proud():
    x=d.readRegister(0)
    return x/float(R)
x=0

while proud()<0.001:
    x=x+50
   
    d.getFeedback(u3.DAC0_16(Value = x))
    
for i in range(200):
    if proud()>0.001:
        x=x-1
        d.getFeedback(u3.DAC0_16(Value = x))
    elif proud()<0.001:
        x=x+1
        d.getFeedback(u3.DAC0_16(Value = x))
    t.sleep(0.063)
        
t.sleep(0.5)       


print proud(), 2*d.readRegister(5000)-d.readRegister(0)
d.writeRegister(5000,0)

        






