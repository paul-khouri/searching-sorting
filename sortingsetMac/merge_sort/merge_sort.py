import math


# ------------- not part of algorithm --- used to check if list is ordered
def checkOrder(A):
    check=True
    for i in range(1,len(A)):
        if(A[i-1]>A[i]):
            check=False
            return check
    return check
#-----------------------------------------------

def copytoNewArray(A,l,u):
    temp=[]
    for m in range(l,u+1):
        temp.append(A[m])
    temp.append(math.inf)
    return temp


def merge(A,p,q,r):
    print(A[p:q+1], end ="")
    print(A[q+1:r + 1], end="")
    print("")
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
        if B[i] <= C[j]:
            A[k]=B[i]
            i += 1
        else:
            A[k]=C[j]
            j += 1
    return


def merge_sort(A,p,r):
    #print(A[p:r+1])
    if p >= r:
        return
    q= math.floor((p+r)/2)
    merge_sort(A, p, q)
    merge_sort(A, q+1,r)
    merge(A, p, q, r)
    return A



A=[1,3,5,7,2,4,6,8]
A=[12,9,3,7,14,11,6,2,10,5]

L=merge_sort(A,0,len(A)-1)
print(L)