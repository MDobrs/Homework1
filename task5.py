def my_func():
    res = 0
    while True:
        numbers = input('Введите числа через пробел или # , чтобы выйти: ').split()
        for i in numbers:
            try:
                if i == '#':
                    print(f'Сумма равна {res}. Выход')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Введите число или #')
        print(f'Сумма равна {res}')


print(my_func())