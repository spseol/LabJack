"""DAC0 =  5000; DAC1 = 5002;
proud(0) = Ib; proud(1) = Ic;
mereni.. vystup je [napeti,proud]
"""
import u3
import matplotlib.pyplot as p




import time as t

d=u3.U3()
d.configU3()

def vstup():
    q=True
    S = []
    while q==True:

        i =input("fdf: ")

        if i>=0:
            S.append(i)
        else:
            break
    S.sort()
    return S
def proud(q,w=0):


    if q == 0 or q=="b":
        e=d.readRegister(0)
        x=d.readRegister(5000)*0.3148089674771077
        r=100
        u=x - e
        I=float(u)/float(r)

    elif q == 1 or q=="c":
        e = d.readRegister(2)
        x=2*d.readRegister(5002)
        r=51.1
        u = x - e
        I = float(u) / float(r)
    if w==0:
        return I
    elif w==1:
        return [e,I]
def proudprm(q,p=30):
    e=[]
    for i in range(p):
        e.append(proud(q))

    return sum(e)/float( len(e))
def iterace(i):
    x=0

    while proud(0) < i:
        x = x + 50

        d.getFeedback(u3.DAC0_16(x))

    for i in range(50):


        if proud(0) > i:
            x = x - 2
            d.getFeedback(u3.DAC0_16(x))
        elif proud(0) <i:
            x = x + 2
            d.getFeedback(u3.DAC0_16(x))
        t.sleep(0.063)

    for i in range(20):
        if proud(0) > i:
            x = x - 1
            d.getFeedback(u3.DAC0_16(x))
        elif proud(0) < i:
            x = x + 1
            d.getFeedback(u3.DAC0_16(x))
        t.sleep(0.07)
def mereni():
    d.writeRegister(5002,0)
    I=[]
    U=[]
    q = 0


    while q<65535:
        for i in range(3):

            x=proud(1)
            U.append(d.readRegister(2))
            I.append(x)
            d.getFeedback(u3.DAC1_16(q))
        q+=10
        t.sleep(0.0001)
    q=0


    return [U,I]




d.writeRegister(5000,0)
d.writeRegister(5002,0)
U=[]
I=[]
v= [0.001]
print "start"
for i in v:
    d.writeRegister(5000, 0)
    d.writeRegister(5002, 0)
    t.sleep(1)

    iterace(i)

    print "iter-done"
    b=mereni()
    print "me-done"
    U.append(b[0])
    I.append(b[1])

d.writeRegister(5000,0)
d.writeRegister(5002,0)
for i in range(len(v)):
    p.plot(U[i],I[i])

print U[0],I[0]
p.show()