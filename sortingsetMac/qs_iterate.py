import math
import random
import time
import threading
from threading import Timer

def checkOrder(A):
    check=True
    for i in range(1,len(A)):
        if(A[i-1]>A[i]):
            check=False
            return check
    return check

def swap(A,x,y):
    temp=A[x]
    A[x]=A[y]
    A[y]=temp
    return A

def partition(A,p,r):
    if p>= r:
        return None
    q=p
    for u in range(p,r):
        if A[u]<=A[r]:
            print(A)
            A=swap(A,q,u)
            print(A)
            q+=1
    A=swap(A,q,r)
    return q

def quickSort_I(A,p,r):
    qStack=[]
    s="length of stack is {0:2d}".format(len(qStack))
    print(s)
    if len(A)<2:
        return A
    m=partition(A,p,r)
    qStack.append((p,m-1))
    qStack.append((m+1,r))
    while len(qStack)!=0:
        (l,u)=qStack.pop()
        m=partition(A,l,u)
        if m is not None:
            qStack.append((l,m-1))
            qStack.append((m+1,u))
    return A

    

    
#if foo is None:
a=[5,9,0,7,6]
b=[2,1,1,2]
c=[3,3,3,3,3,3,3]
d=[]
e=[3]
f=[6,0,5,8,2,2]
g=[]
h=[5,9,11,1,7,3]
for i in range(0,100000):
    g.append(random.randint(0, 10000))
    #g.append(-i)

y=h
print(y)
print("Start sort")
y=quickSort_I(y,0,len(y)-1)
print("Sorting completed")
print(y)
print(checkOrder(y))



##myStack=[]
##p=3
##r=5
##myStack.append((p,r))
##p=myStack.pop()
##print(p[0])
##print(p[1])
###y=f
###m=partition(y,0,len(y)-1)
##print(y)
###print(m)
