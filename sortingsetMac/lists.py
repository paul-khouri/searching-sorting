import math
import random
import time
import threading
from threading import Timer




a=[]
for i in range(0,10000):
    a.append(random.randint(0, 1000))
print("Array filled")


def insertInto(A,x):
    k=len(A)-1
    if(x<A[0]):
        A.insert(0,x)
    else:
        while (x<A[k] and k>0):
            k-=1
        A.insert(k+1,x)
    return A
    
def checkOrder(A):
    check=True
    for i in range(1,len(A)):
        if(A[i-1]>A[i]):
            check=False
            return check
    return check
        
print("Start Sort")
ticks=time.time()

subList=[a[0]]
for i in range(1,len(a)):
    subList=insertInto(subList, a[i])

ticksA=time.time()
print(ticksA)
difference=ticksA-ticks
print(difference)
print("Sorting Completed")
print(checkOrder(subList))
print(checkOrder(a))

ticks=time.time()
print(ticks)
def hello():
    print("Hello World")
    ticksA=time.time()
    print(ticksA)
    difference=ticksA-ticks
    print(difference)
#t=Timer(10.0, hello)
#t.start()
