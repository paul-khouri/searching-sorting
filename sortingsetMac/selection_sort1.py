# Find the smallest item in the unsorted list,
# remove it and place it in the sorted list
#Find the smallest item in the remaining unsorted list,
# remove it and place it at the end of the sorted list
#Continue until the unsorted list is empty
z = [5,9,11,3,12,7,-1, 7, -12, 8,8,8,8,8,8]
y= [9,7,5,11,12,2,14,3,10,6]
L = y
S = []
print("{};".format(L))
checks_total = 0
while len(L)>0:
    temp = L[0]
    i = 0
    while i < len(L):
        if L[i] < temp:
            temp = L[i]
        i += 1
    L.remove(temp)
    S.append(temp)
    print(L, end='')
    print(S, end='')
    checks_total += i
    print("; Checks = {}".format(i))
print(";Total Checks = {}".format(checks_total))


