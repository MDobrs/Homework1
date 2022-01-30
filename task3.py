def my_func(a1, a2, a3):
    my_list = [a1, a2, a3]
    my_list.sort()
    return my_list[1] + my_list[2]


x = int(input('Введите число: '))
y = int(input('Введите число: '))
z = int(input('Введите число: '))

print(my_func(x, y, z))