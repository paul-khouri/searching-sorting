import random
import time

from setfortests.sortingset import selection_sort, checkOrder, insertion_sort, quick_sort, \
    insertion_sort_in_place, merge_sort

g=[]
count = 1
start = 0
end=0
time_set = {}
my_choice = 5
while count<10:
    g=[]
    for i in range(0, count*1000):
        g.append(random.randint(0, 1000000))
    start = time.time()
    if my_choice == 1:
        L=selection_sort(g)
    elif my_choice == 2:
        L=insertion_sort(g)
    elif my_choice == 3:
        L=insertion_sort_in_place(g)
    elif my_choice == 4:
        L= quick_sort(g, 0, len(g)-1)
    elif my_choice == 5:
        L= merge_sort(g, 0, len(g)-1)
    end = time.time()
    print(end-start)
    time_set[len(L)]=end-start
    print(checkOrder(L))
    count+=1
print(time_set)
if my_choice == 1:
    f="selectionTime.txt"
elif my_choice == 2:
    f = "insertionTime.txt"
elif my_choice == 3:
    f = "insertionplaceTime.txt"
elif my_choice == 4:
    f = "quickTime.txt"
elif my_choice == 5:
    f = "mergeTime.txt"

out_file=open(f, 'w')
for x, y in time_set.items():
    out_file.write("{},{}\n".format(x, y))
out_file.close()
