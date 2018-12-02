#Take the first item from your unsorted list, remove it and place it in the sorted list
#Take the next item in the unsorted list and insert it into the right place in the sorted list
#Do this until the unsorted list is empty
x=[5,9,11,3,12,7,-1, 7, -12, 8,8,8,8,8,8]
z=[5,4,1,7,3,0,6,2,9,8]
y= [9,7,5,11,12,2,14,3,10,6]
L = y
S=[]
print(L, end='')
print("{} ;".format(S))
S.append(L[0])
L.remove(L[0])
print(L, end='')
print("{} ;".format(S))
total_checks = 0
while len(L)>0:
    i = len(S)-1
    check_count = 1
    while i >= 0 and L[0] < S[i] :
        i -= 1
        check_count += 1
    total_checks += check_count
    S.insert(i+1, L[0])
    L.remove(L[0])
    print(L, end='')
    print(S, end='')
    print("; Checks = {}".format(check_count))

print("; Total Checks = {}".format(total_checks))