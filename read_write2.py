from random import randint
my_list=["0001", "0002", "0003"]
my_large_list = []
current_file_name = "orderednumbers.txt"

# file list line n elements per line
def file_writer(f,a,n):
    file_name = f
    out_file=open(file_name, 'a')
    i = 0
    for l in a:
        out_file.write(l)
        i += 1
        if i % n == 0:
            out_file.write("\n")

    out_file.close()


def file_clear(f):
    file_name = f
    out_file=open(file_name, 'w')
    out_file.write("")
    out_file.close()


#file_writer("textone.txt", my_list, 10)
file_clear(current_file_name)


for i in range(0,1500):
    t_num = randint(0,1000000)
    my_string = " {} ".format(str(t_num).zfill(6))
    my_large_list.append(my_string)

#print(my_large_list)
my_large_list.sort()
file_writer(current_file_name, my_large_list, 10)

