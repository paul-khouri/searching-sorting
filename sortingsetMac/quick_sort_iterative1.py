import random
y= [5,9,11,1,7,3]
z=[5,4,1,7,3,0,6,2,9,8]
x=[16,19,2,51,90,78,31,746,88,35,11,26,98,214, 983, 54, 21, 908]
w=[9,8,7,6,5,4,3,2,1,0]
v=[5,9,2,0,7,8,3,6,1,4]
q_stack = []

# ------------- not part of algorithm --- used to check if list is ordered
def checkOrder(A):
    check=True
    for i in range(1,len(A)):
        if(A[i-1]>A[i]):
            check=False
            return check
    return check
#--------not part of the algorithm used to print the list with pivots----------------


def print_with_pivots(A, p_list,checks):
    p_list.sort()
    my_string = "{}".format(A[:p_list[0]])
    for i in range(0, len(p_list) - 1):
        my_string = "{}{}{}".format(my_string, A[p_list[i]], A[p_list[i] + 1:p_list[i + 1]])
    my_string = "{}{}{}".format(my_string, A[pivot_list[len(p_list) - 1]], A[p_list[len(p_list) - 1] + 1:])
    print("{} Checks = {} ".format(my_string,checks))

#------------------------------------------------------------------------
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
    pivot_list.append(p)
    #print(pivot_list)
    print_with_pivots(L,pivot_list,checks)
    #print("{}{}{}{}".format(L[:p],L[p],L[p+1:upper+1],L[upper+1:]))
    #print(L, end="")
    #print("{},{}".format(lower,upper))

    return p


def quick_sort(L, lower , upper):
    # start the stack with the all indexes covered
    q_stack.append((lower, upper))
    while len(q_stack) !=0:
        #print(q_stack)
        (l, u) = q_stack.pop()
        p = partition(L,l,u)
        # print(p)
        if p is not None:
            q_stack.append((l,p-1))
            q_stack.append((p+1,u))
g=[]
for i in range(0,100):
    g.append(random.randint(0, 10000))
g=v
pivot_list = []
print(g)
quick_sort(g, 0, len(g)-1)
print(checkOrder(g))