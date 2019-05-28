from math import floor , log2 , ceil
import time




def read_file_to_list(file_name):
    """ reads a given file name and places items in list
        splits on spaces removes empty strings and line breaks """
    out_file = open(file_name, 'r')
    L = []
    for x in out_file:
        temp = x.split(" ")
        for y in temp:
            if len(y) != 0 and y != "\n":
                L.append(y)
    return L


def binary_search( A , item):
    lower = 0
    upper = len(A)
    index = floor((lower+upper)/2)
    flag = True
    while flag:
        if A[index] == item:
            return index
        elif upper-lower <= 1:
            return "Not Found"
        elif item < A[index] :
            #print("{1} is less than {0} <-".format(A[index], item))
            upper = index
            index = floor((lower+upper)/2)
        else:
            #print("{1} is greater than {0} ->".format(A[index], item))
            lower = index
            index = floor((lower + upper) / 2)

file_read = "ten_sorted.txt"
file_read = "million_sorted.txt"
search_item = "12719603"
search_item = "07085132"
A = read_file_to_list(file_read)
start = time.time()
print(binary_search(A, search_item))
end = time.time()
print(end-start)
