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


def copytoNewArray(A,l,u):
    temp=[]
    for m in range(l,u+1):
        temp.append(A[m])
    temp.append(math.inf)
    return temp
checks=0
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
        global checks
        checks+=1
        if B[i]<=C[j]:
            A[k]=B[i]
            i+=1
        else:
            A[k]=C[j]
            j+=1
    return A



def mergeSort_I(A):
    if len(A)<2:
        return A
    extraElement=False
    if len(A)%2!=0:
        A.append(math.inf)
        extraElement=True
    s=[]
    for i in range (0,len(A)-1,2):
        s.append((i,i,i+1))
        #print(s)
    while len(s)>1:
        k=len(s)-1
        for j in range(0,k+1):
            #print("{},{},{}".format(s[j][0],s[j][1],s[j][2]), end="")
            A=merge(A,s[j][0],s[j][1],s[j][2])
            #print(A)
        while k>0:
            s[k-1]=(s[k-1][0],s[k-1][2],s[k][2])
            s.pop(k)
            k-=2
    A=merge(A,s[0][0],s[0][1], s[0][2])
    #print(A)
    if extraElement:
        A.pop()
    return A

#lastIndex
#make array even in length
#range from 0 to length-1

x=[12,9,3,7,14,11,6,2,1,1]
y=[]
z=[5]
w=[9,7]
v=[12,9,3,7,14,11,6,2,6,6,1]
g=[]
for i in range(0,300001):
    g.append(random.randint(0, 10000))
c=g
#print(c)
print("Start Sort")
startTime =time.time()
c=mergeSort_I(c)
endTime = time.time()
print("Sorting completed")
print(endTime - startTime)
#print(c)
print(checkOrder(c))
print(checks)
