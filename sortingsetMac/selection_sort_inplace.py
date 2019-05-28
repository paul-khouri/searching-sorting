z = [5,9,11,3,12,7,-1, 7, -12, 8,8,8,8,8,8]
y= [9,7,5,11,12,2,14,3,10,6]
L = y
dict = {}

def selection_sort_in_place(list):
    for i in range(0, len(list)-1):
        smallest = i
        count = 0
        for j in range(i+1,len(list)):
            count += 1
            if list[j] < list[smallest]:
                smallest = j
        dict[i] = count
        list = swap(list, i,smallest)
        print(list)
    return list


def swap(list , i,j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    return list

L=selection_sort_in_place(L)
print(dict)
