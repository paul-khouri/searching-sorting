import math
import random
import time
import threading
from threading import Timer
def swap(A,x,y):
    temp=A[x]
    A[x]=A[y]
    A[y]=temp
    return A


def checkOrder(A):
    check=True
    for i in range(1,len(A)):
        if(A[i-1]>A[i]):
            check=False
            return check
    return check

def qSort(A,lower,upper):
    if(upper<=lower):
        return
    if(upper-lower==1):
        if(A[lower]==A[upper]):
            return
        elif(A[lower]<A[upper]):
            return
        else:
            A=swap(A,lower,upper)
            return
    pivot=A[upper]
    L=lower
    U=upper
    count=0
    while L<U:
        print(count)
        s="L:{0:3d} U{1:3d}: A[L]:{3:3d} A[U]:{4:3d} pivot:{2:3d}".format(L,U,pivot,A[L],A[U])
        print(s)
        count+=1
        if(count==40):
            return
        while A[L]<=pivot:
            L=L+1
        while A[U]>=pivot:
            U=U-1
        A=swap(A,L,U)
        
    #s=",".join(str(x) for x in a)
    #print(s)
    #outString="L is {0:5d}, U is {1:5d} lower is {2:5d} upper is {3:5d}".format(L, U, lower, upper)
    #print(outString)
    #ucall="A, U+1:{0:2d} ,upper:{1:2d}".format(U+1,upper)
    #print(ucall)
    #lcall="A, lower:{0:2d} ,L-1:{1:2d}".format(lower,L-1)
    #print(lcall)
    
    qSort(A,U+1,upper)
    qSort(A,lower,L-1)
    

#--------body--------------
a=[]
#a= ["3","7","14","52","63","60","36","87","60","93","32"]
#a= ["63","60"]
#a= [int(i) for i in a]
#a=[int(3),int(5),int(1),int(8),int(7),int(-9),int(11),int(6)]

for i in range(0,30):
    a.append(random.randint(0, 100))
s=";".join(str(x) for x in a)
print(s)
#print(len(a)-1)    
qSort(a,0,len(a)-1)
s=",".join(str(x) for x in a)
print(s)
print(checkOrder(a))

            
