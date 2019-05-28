import math

def selection_sort(L):
    S=[]
    while len(L) > 0:
        temp = L[0]
        i = 0
        while i < len(L):
            if L[i] < temp:
                temp = L[i]
            i += 1
        L.remove(temp)
        S.append(temp)
    return S


def insertion_sort(L):
    S = []
    S.append(L[0])
    L.remove(L[0])
    while len(L) > 0:
        i = len(S) - 1
        check_count = 1
        while i >= 0 and L[0] < S[i]:
            i -= 1
        S.insert(i + 1, L[0])
        L.remove(L[0])
    return S

def insertion_sort_in_place(list):
    for i in range(1, len(list)):
        key = list[i]
        j= i-1
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            list[j] = key
            j -= 1
    return list


def insertion_sort_inplace(L):
    p = 1
    while p < len(L):
        i = 0
        while L[p] > L[i] and i <= p:
            i += 1
        temp = L[p]
        L.pop(p)
        L.insert(i, temp)
        p += 1
    return L


def partition(L,lower, upper ):
    if lower >= upper:
        return None
    p = lower
    checks = 0
    #print(L[lower:upper+1])
    for i in range(lower, upper):
        checks += 1
        if L[i] <= L[upper]:
            # swap L[i] with L[p]
            temp = L[i]
            L[i] = L[p]
            L[p] = temp
            # move dividing index up by one
            p += 1
    # when all done swap the last value (the pivot) with the value at the
    # the dividing index
    temp = L[p]
    L[p] = L[upper]
    L[upper] = temp
    # return the dividing index
    return p


q_stack = []


def quick_sort(L, lower , upper):
    # start the stack with the all indexes covered
    q_stack.append((lower, upper))
    while len(q_stack) !=0:
        (l, u) = q_stack.pop()
        p = partition(L,l,u)
        if p is not None:
            q_stack.append((l,p-1))
            q_stack.append((p+1,u))
    return L


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
        if B[i] <= C[j]:
            A[k]=B[i]
            i += 1
        else:
            A[k]=C[j]
            j += 1
    return


def merge_sort(A,p,r):
    if p >= r:
        return
    q= math.floor((p+r)/2)
    merge_sort(A, p, q)
    merge_sort(A, q+1,r)
    merge(A, p, q, r)
    return A


# ------------- not part of algorithm --- used to check if list is ordered
def checkOrder(A):
    check=True
    for i in range(1,len(A)):
        if(A[i-1]>A[i]):
            check=False
            return check
    return check
