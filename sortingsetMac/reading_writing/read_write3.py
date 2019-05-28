from random import randint



def file_writer(f,a,n):
    """ writes a file
        parameters: file name , list to write to file, number of elements per line 
        returns none """
    file_name = f
    out_file=open(file_name, 'w')
    i = 0
    for l in a:
        out_file.write("{}  ".format(l))
        i += 1
        if i % n == 0:
            out_file.write("\n")
    out_file.close()


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


def file_clear(f):
    file_name = f
    out_file=open(file_name, 'w')
    out_file.write("")
    out_file.close()


def create_random_list(number_elements):
    L = []
    for i in range(0, number_elements):
        t_num = randint(0, 10000)
        my_string = "{}".format(str(t_num).zfill(8))
        L.append(my_string)
    return L





unsorted_file_name = "hundred_unsorted.txt"
sorted_file_name = "hundred_sorted.txt"
num_elements = 100
my_large_list = create_random_list(num_elements)

#my_large_list = read_file_to_list(read_file_name)
file_writer(unsorted_file_name, my_large_list, 4)
my_large_list.sort()
file_writer(sorted_file_name, my_large_list, 4)

#print(my_large_list)
#my_large_list.sort()
#


