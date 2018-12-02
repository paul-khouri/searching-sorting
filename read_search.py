current_file_name = "orderednumbers.txt"
txt_list=[]
to_find = "148207"
file_name = current_file_name
out_file = open(file_name, 'r')


for x in out_file:
    temp = x.split(" ")
    for y in temp:
        if len(y) !=0 and y!="\n":
            txt_list.append(y)


def linear_search( A , item):
    for i in range(0, len(A)):
        if item == A[i]:
            print("Found at index {}".format(i))
            return True
    print("Not found")
    return False

linear_search(txt_list , to_find)