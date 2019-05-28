from math import floor , log2 , ceil
current_file_name = "orderednumbers.txt"
txt_list=[]
to_find = "703120"
file_name = current_file_name
out_file = open(file_name, 'r')


for x in out_file:
    temp = x.split(" ")
    for y in temp:
        if len(y) !=0 and y!="\n":
            txt_list.append(y)


def binary_search( A , item):
    lower = 0
    upper = len(A)
    index = floor((lower+upper)/2)
    flag = True
    while flag:
        if A[index] == item:
            return True
        elif upper-lower <= 1:
            return False
        elif item < A[index] :
            print("{1} is less than {0} <-".format(A[index], item))
            upper = index
            index = floor((lower+upper)/2)
        else:
            print("{1} is greater than {0} ->".format(A[index], item))
            lower = index
            index = floor((lower + upper) / 2)

print("The number of items in the list is {}".format(len(txt_list)))
print("The maximum number of checks should be {}".format( ceil(log2(len(txt_list))) ) )
print("Searching for {}".format(to_find))
if binary_search(txt_list , to_find):
    print("Found")
else:
    print("Item is not in the list")