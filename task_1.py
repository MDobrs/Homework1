my_list = ['name', 1889, 3.14, False]
i = 0
b = len(my_list)
while i >= 0:
    a = my_list[i]
    i+=1
    print(type(a))
    if i==b:
        break