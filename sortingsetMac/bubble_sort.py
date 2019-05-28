my_list=[10,9,8,7,6,5,4,3,2,1]

k = 1
while k < len(my_list):
    i = 0
    swapped = False
    while i < len(my_list)-1:
        if my_list[i+1] < my_list[i]:
            temp = my_list[i+1]
            my_list[i+1] = my_list[i]
            my_list[i] = temp
            swapped = True
        i += 1
    print("{} Pass: {}".format(my_list, k))
    if swapped == False:
        print("Done in {} passes".format(k))
        break
    elif k == len(my_list) - 1:
        print("Done in {} passes".format(k))
    k += 1

print(my_list)