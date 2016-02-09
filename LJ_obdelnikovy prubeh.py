# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 16:18:10 2016

@author: XAXA
"""


import time as t
import u3
d = u3.U3()
d.configU3()
DAC0=5000

T=input("Zadejte frekvenci v Hz: ")
DCL=input("Zadejte DCL v %: ")
u=input("Zadejte Umax(0-5): ")
Th=T*DCL/100
Tl=T-Th

print "start"
while t.clock()<30:
    d.writeRegister(DAC0,u)
    t.sleep(Th)
    d.writeRegister(DAC0,0)
    t.sleep(Tl)