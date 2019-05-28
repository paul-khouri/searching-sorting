#step through the list and compare adjacent pairs
#swap them if they are in the wrong order.
#repeatedly pass through the list until the list is sorted.
x= [10,9,8,7,6,5,4,3,2,1]
z = [1,2,3,4,5,6,7,8,9,10]
y= [9,7,5,11,12,2,14,3,10,6]
L= y
print(";{};".format(L))
k = 1
checks =0
while k < len(L):
    i = 0
    swapped = False
    while i < len(L)-k:
        if L[i+1] < L[i]:
            temp = L[i+1]
            L[i+1] = L[i]
            L[i] = temp
            swapped = True
        i += 1
    checks += i
    print("Pass: {} ; {} ; Checks: {}".format(k, L, i))
    if swapped == False:
        print("Done in {} passes ; ; Total Checks: {}".format(k, checks))
        break
    elif k == len(L) - 1:
        print("Done in {} passes ; ; Total Checks: {}".format(k, checks))
    k += 1