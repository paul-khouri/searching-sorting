import time
import sys
sys.setrecursionlimit(100000)
current_file_name = "ten_unsorted.txt"
current_file_name = "ten_thousand_unsorted.txt"
current_file_name = "hundred_unsorted.txt"
#current_file_name = "million_unsorted.txt"

txt_list=[]
# for ten unsorted
to_find = "03568134"
to_find = "04054464"
to_find = "14054464"
# for hundred unsorted
to_find = "04652846"
#for ten thousand unsorted
#to_find = "09991156"
# for million unsorted
#to_find = "03922257"
#to_find = "00263243"
#to_find = "09798217"
#to_find = "19798217"
file_name = current_file_name
out_file = open(file_name, 'r')

count=0
for x in out_file:
    temp = x.split(" ")
    for y in temp:
        if len(y) !=0 and y!="\n":
            txt_list.append(y)
            count+=1
#print(count)


#2 tests
def linear_search( A , item):
    #test if i is in range
    for i in range(0, len(A)):
        #test if item is A[i]
        if item == A[i]:
            print("Found at index {}".format(i))
            return True
    print("Not found")
    return False

def sentinal_linear_search(A, item):
    n = len(A)-1
    last = A[-1]
    A[-1] = item
    i = 0
    # one check only
    while A[i] != item:
        i += 1
    A[-1] = last
    if i < n or A[n] == item:
        print("Found at index {}".format(i))
        return i
    else:
        print("Not found")
        return -1


def recursive_linear_search(A,n,i, item):
    if i > n:
        return "Not found"
    if A[i] == item:
        return i
    else:
        return recursive_linear_search(A, n, i+1, item)




#start = time.time()
#print( recursive_linear_search(txt_list ,len(txt_list)-1, 0, to_find) )
#finish = time.time()
#print(finish - start)


start = time.time()
linear_search(txt_list , to_find)
finish = time.time()
print(finish - start)

# start = time.time()
# sentinal_linear_search(txt_list,to_find)
# finish = time.time()
# print(finish - start)
