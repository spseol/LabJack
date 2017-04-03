# -*- coding: utf-8 -*-
"""
Created on Fri Feb 05 14:00:48 2016

@author: XAXA
"""

import time as t
import u3
d = u3.U3()
d.configU3()
import pylab
from pylab import pi,sin

print "Pristroj funguje pouze na napeti 0-5 V"

DAC0=5000    
    
   
q=0

while q==0:
    
    print "  ~: s, -_-_-_: o, /\/\/\: p "
    q=raw_input("Zvolte tip prubehu, pro vypnuti zadejte k - ")
    """ SINUS """
    if q=="s":
        T=input("Zadejte dobu trvana funkce v sekundách: ")
        a=input("Zadejte Umax(0-5): ")
        f=input("Zadejte frekvenci: ")
        a=a/2
        
        print "\nspuštím ..."
        
        d.writeRegister(DAC0,a)
        t.sleep(0.8)
        cas= t.clock()
        print "\nstart"
        while T+cas>t.clock():
            u=a*sin(f*2*pi*(t.clock()-cas))+a
            d.writeRegister(DAC0,u)
        
        else:
            d.writeRegister(DAC0,0)
            print "Konec"
            q=0
            """OBDELNIK"""
    elif q=="o":
        
        t1=input("Zadejte dobu trvana funkce v sekundach >4: ")
        f=input("Zadejte frekvenci: ")
        DCL=input("Zadejte DCL v %: ")
        u=input("Zadejte Umax(0-5): ")
        T=1/float(f)
        Th=T*DCL/100
        Tl=T-Th
        cas= t.clock()
        
        print "start"
        while t1+cas>t.clock():
            d.writeRegister(DAC0,u)
            t.sleep(Th)
            d.writeRegister(DAC0,0)
            t.sleep(Tl)
        d.writeRegister(DAC0,0)
        print "Konec"
        q=0
        """PILA"""    
    elif q=="p":
        cas= t.clock()
        U=5
        T=input("Zadejte dobu trvana funkce v sekundach: ")
        f=input("Zadejte frekvenci: ")
        
        
        per=1/float(f)
        d.writeRegister(DAC0,0)
        t1=0
        z=0
        n=0


    
        d.writeRegister(DAC0, 5)        
        t.sleep(0.3)    
        while T+cas>t.clock():
            
    
    
    
            print t1    
            if t1>=per:       
                n=n+1       
            t1=(t.clock()-cas)-per*n       
            u= abs(10*f*t1-U )        
        
        
            d.writeRegister(DAC0,u)
        
        d.writeRegister(DAC0,0)
        print "Konec"
        q=0
        
        
    
    elif q=="k":
        print " Ukoncuji"
        t.sleep(1)
    else:
        print "Neplatny prikaz..."
        q=0
