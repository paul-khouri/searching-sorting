import math
import random
import time
import threading
from threading import Timer





#---------------Insertion sort methods-------
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
#------------------------------------------        
for j in range(5000,20000,1000):
    a=[]
    for i in range(0,j):
        a.append(random.randint(0, 1000))
    #print("Array filled")
    alength=len(a)
    #print("Start Sort")
    ticks=time.time()
    #print(ticks)
    #------ sort
    subList=[a[0]]
    for i in range(1,len(a)):
        subList=insertInto(subList, a[i])
    #--------
    ticksA=time.time()
    #print(ticksA)
    difference=ticksA-ticks
    #print(difference)
    #print("Sorting Completed")
    outString="The sort took {0:5.2f} seconds to complete and there were {1:5d} elements in the list".format(difference, alength)
    print(outString)
    #print(checkOrder(subList))
    #print(checkOrder(a))



