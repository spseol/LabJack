# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 19:14:20 2016

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
iiz=[]
iiiz=[]
i=0
ii=0
R=329
t.sleep(0.4)
u=0

while 1000*(ii-i)/float(R) <15:
    u=u+0.05

    i=d.readRegister(I)
    ii=d.readRegister(II)
    iii=d.readRegister(III)
    iz.append(i)
    iiz.append(ii)
    iiiz.append(iii)
    d.writeRegister(V,u) 
    t.sleep(0.1)



i=pylab.array(iz)
ii=pylab.array(iiz)
iii=pylab.array(iiiz)
U=iii-ii
Imp=1000*(ii-i)/float(R)

Uz=[]
Iz=[]


t.sleep(1)
d.writeRegister(V,0)    
pylab.plot(U,Imp)    
pylab.title('Cervena LED')
pylab.grid(True)
pylab.xlabel('U (V)')
pylab.ylabel('I (mA)')
for i in U:
    Uz.append(i)
for i in Imp:
    Iz.append(i)
    
    
    
print Uz
print Iz
    






pylab.show()

    
    


