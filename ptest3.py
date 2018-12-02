import math
import random


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

def selectionSort(A):
    #find position of smallest   value in array
    for k in range(0,len(A)):
        temp=A[k]
        tempIndex=k
        for i in range(k,len(A)):
            if A[i]<temp:
                temp=A[i]
                tempIndex=i
                A=swap(A,k,tempIndex)
        #print("Lowest value: ",temp, "; Index of lowest value: ", tempIndex, sep=" ",end="\n") 
    return A
        
    
    
a=[]
b=[]
for i in range(0,1000):
    x=random.randint(0, 100)
    a.append(x)
for j in range(0,100):
    b.append(100-j)
print(b)

#a=selectionSort(a)
#a=bubbleSort(a)
b=bubbleSort(b)    
print(b)
        
    

