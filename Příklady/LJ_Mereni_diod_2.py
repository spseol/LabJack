# -*- coding: utf-8 -*-
"""
Created on Mon May 16 10:43:12 2016

@author: XAXA
"""

import pylab
import time as t
import u3
d= None
d = u3.U3()
d.configU3()

I= 0
II= 2
III= 4
IV= 6
V= 5000
VI= 5002
d.writeRegister(V,0)
iz=[]
uz=[]
i=0

R=227
t.sleep(0.4)
u=0.25


while 1000*i/float(R)<12:
    u=u+0.02
    if u<0.8:    
        uz.append((u*2)+0.04)
    elif u<1.6 and u>=0.8:
        uz.append((u*2)+0.05)
    elif 1.6<=u<2.3:
        uz.append((u*2)+0.06)
    else:
        uz.append((u*2)+0.07)
    t.sleep(0.2)
    
    
    i=d.readRegister(I)

    iz.append(i)
    
    d.writeRegister(V,u) 
    



i=pylab.array(iz)
u=pylab.array(uz)
Proud=i/float(R)
U=u-i



Uz=[]
Iz=[]


t.sleep(1)
d.writeRegister(V,0)    
pylab.plot(U,Proud)    
pylab.title('Cervena LED')
pylab.grid(True)
pylab.xlabel('U (V)')
pylab.ylabel('I (mA)')
for i in U:
    Uz.append(i)
for i in Proud:
    Iz.append(i)
    
    
    
print Uz
print Iz
    






pylab.show()