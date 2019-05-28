import math
import random

max=1
for i in range(0,10):
    for k in range(1,max):
        x=10*i+k
        y=str(x)
        if x%6==0:
            print("---",end=",")
        else:
            z=y.zfill(3)
            print(z,end=",")
    print(end='\n')

#p=input("Please enter a number: ")
#print(p)
def swap(A,x,y):
    temp=A[x]
    A[x]=A[y]
    A[y]=temp
    return A

def bubbleSort(A):
    for k in range (1,len(A)):
        for i in range (0,len(A)-k):
           if A[i+1]<A[i]:
               A=swap(A,i,i+1)
    return A
    
a=[]
for i in range(0,100):
    x=random.randint(0, 100)
    a.append(x)
print(a)
a=swap(a,0,1)
print(a)
print(len(a))
a=bubbleSort(a)
print(a)
        
    

