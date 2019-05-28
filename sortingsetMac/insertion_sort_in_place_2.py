z = [5,9,11,3,12,7,-1, 7, -12, 8,8,8,8,8,8]
y= [9,7,5,11,12,2,14,3,10,6]
y= [9,7,5,11,12,2,14,3,10,6]
L = y
dict = {}


def insertion_sort_in_place(list):
    for i in range(1, len(list)):
        key = list[i]
        j= i-1
        count = 0
        while j >= 0 and list[j] > key:
            count +=1
            list[j+1] = list[j]
            j -= 1

        dict[i] = count
        list[j+1] = key
        print(list , end ="")
        print("{} books are sorted".format(i+1))
    return list
print(L)
L=insertion_sort_in_place(L)
print(L)
print(dict)

