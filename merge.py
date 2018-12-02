import math
import random
import time
import threading
from threading import Timer



def copytoNewArray(A,l,u):
    temp=[]
    for m in range(l,u+1):
        temp.append(A[m])
    temp.append(math.inf)
    return temp


def merge(A,p,q,r):
    if len(A)<2:
        return A
    if p>q or q>=r:
        print ("p,q,r error")
        return
    B=copytoNewArray(A,p,q)
    C=copytoNewArray(A,q+1,r)
    i=0
    j=0
    for k in range(p,r+1):
        if B[i]<=C[j]:
            A[k]=B[i]
            i+=1
        else:
            A[k]=C[j]
            j+=1
    return A


u=[]
v=[3]
w=[0]
x=[2,3,4,7,9,11,31,80]
y=[0,0,3,5,7,21,22,23,67,81]
xLarge=[]
yLarge=[]
startingX=0
startingY=0
for i in range (0,100):
    startingX+=random.randint(0, 10000)
    xLarge.append(startingX)
for j in range (0,50):
    startingY+=random.randint(0,10000)
    yLarge.append(startingY)


c=xLarge
d=yLarge
p=0
q=len(c)-1
r=len(c)+len(d)-1
e=c+d
print(e)
e=merge(e,p,q,r)
print(e)

