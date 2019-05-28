z = [5,9,11,3,12,7,-1, 7, -12, 8,8,8,8,8,8]
y= [9,7,5,11,12,2,14,3,10,6]
x= [9,7,5,11,12,2,14,3,10,6]
u = [0,1,2,3,4,5,6,7,8,9]
v = [9,8,7,6,5,4,3,2,1,0]
w = [1,2,3,2,1,1,1,2,2,2]

L = w
dict = {}


def insertion_sort_in_place(list):
    for i in range(1, len(list)):
        key = list[i]
        j= i-1
        count = 0
        while j >= 0 and list[j] > key:
            count +=1
            list[j+1] = list[j]
            list[j] = key
            j -= 1
            print("----- {}".format(list))

        dict[i] = count
        print(list , end ="")
        print("{} books are sorted".format(i+1))
    return list
print(L)
L=insertion_sort_in_place(L)
print(L)
print(dict)

