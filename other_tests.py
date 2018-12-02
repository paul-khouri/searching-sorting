A = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
pivot_list = [3,6,9,14]
pivot_list.sort()
print(pivot_list)
my_string = "{}".format(A[:pivot_list[0]])
for i in range(0, len(pivot_list)-1):
    my_string="{}{}{}".format(my_string,A[pivot_list[i]], A[pivot_list[i]+1:pivot_list[i+1]])
    print(i)
my_string="{}{}{}".format(my_string,A[pivot_list[len(pivot_list)-1]],A[pivot_list[len(pivot_list)-1]+1:] )
print(my_string)