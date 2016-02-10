# -*- coding: utf-8 -*-
"""
Created on Fri Feb 05 18:29:13 2016
("Freknvence[Hz]: ")
("Umax: ")
("Umax: ")
@author: XAXA
"""
import pylab
DAC0 = 5000
import time as t
import u3
d = u3.U3()
d.configU3()


f=1
T=[]
bla=[]
per=1/float(f)
d.writeRegister(DAC0,0)
t1=0
z=0
n=0


    
d.writeRegister(DAC0, 5)        
t.sleep(0.3)    
while t.clock()<8:
    
    
    
    print t1
    
    if t1>=per:
        
        n=n+1
        
    t1=t.clock()-per*n
        
    u= abs(10*f*t1-5)
        
        
    d.writeRegister(DAC0,u)

    
        
    
    bla.append(d.readRegister(0))
        
    T.append(t.clock())
    


d.writeRegister(DAC0,0)
pylab.plot(T,bla)

pylab.title('hsdgh')
pylab.grid(True)
pylab.xlabel('t')
pylab.ylabel("u")

pylab.show()
