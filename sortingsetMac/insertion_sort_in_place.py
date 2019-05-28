import random
w=[3,7,1,4,1]
g=[]
for i in range(0,100):
    g.append(random.randint(0, 10000))
L = g
print(L, end="")
p = 1
while p<len(L):
    i = 0
    #print(L, end="")
    print(p)
    while L[p] > L[i] and i <= p:
        i += 1
    temp = L[p]
    L.pop(p)
    L.insert(i, temp)
    print(L, end="")
    print(p, end="")
    print("Checks: {}".format(i+1))
    p += 1


