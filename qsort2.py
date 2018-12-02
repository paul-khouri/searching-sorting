import math
import random
import time
import threading
from threading import Timer
a=[5,9,0,7,6]
b=[2,1,1,2]
c=[3,3,3,3,3,3,3]
e=[6,0,5,8,2,2]
##print(a[3]<-7)#false
##print(a[3]>a[4])#true
##s=int(6)
##print(7<=s)#false
##print(6<=s)#true

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
    q=p
    for u in range(p,r):
        if A[u]<=A[r]:
            A=swap(A,q,u)
            q+=1
    A=swap(A,q,r)
    print(A)
    return q

def quicksort(A,b,t):
    if b>=t:
        return
    m=partition(A,b,t)
    quicksort(A,b,m-1)
    quicksort(A,m+1,t)

d=[]
for i in range(0,100):
    #d.append(random.randint(0, 10000))
    d.append(-i)
    
y=e
print("start sort")
quicksort(y,0,len(y)-1)
print("sort completed")
print(y)
print(checkOrder(y))
            
            
