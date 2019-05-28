import math
import random
print("hello")
a=2
b=12
c=a+b
d=a*b
e=a^b
f=int(math.pow(a,b))
for i in range(-5,64):
    x=math.pow(a,i)
    print(i,x,end='\n')

print(str(c) + str(d))
print(c,d,e,f, sep=',',end='\n')
max=10
for i in range(0,2*max):
    for k in range(0,max):
        x=max-1-i
        if (10*i+k)%7==0:
            print("( ++ )",end="")
        else:
            if i==0:
                print("( 0",k," )",sep='',end="")
            else:
                print("(",10*i+k,")",end="")
    print(end='\n')
a=[]
for i in range(1,10000):
    y=random.random()
    x=random.randint(0,9)
    a.append(x)
    #print(x,y, sep=',')
b=[]
for m in range(0,10):
    ct=a.count(m)
    b.append(ct)
    
#print(a)
a.sort()
#print(a)
print(b)
