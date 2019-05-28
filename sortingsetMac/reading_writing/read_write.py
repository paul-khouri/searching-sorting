my_list=["0001", "0002", "0003"]


def file_writer(f,a):
    file_name = f
    out_file=open(file_name, 'w')
    for l in a:
        temp=l
        print(type(temp))
        print(temp)
        my_string = "{} \n".format(temp)
        out_file.write(my_string)
    out_file.close()


#file_writer("textone.txt", my_list)
for i in range(0,200):
    if i%10 == 0 and i!=0:
        print("\n")
    my_string = "{}  ".format(str(i).zfill(3))
    print(my_string, end ='')

