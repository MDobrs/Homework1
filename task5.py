#5 Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.

my_list = [7, 5, 3, 3, 2]
answer = "yes"
while answer == "yes":
    number = int(input("Введите число: "))
    i=0
    if number in my_list:
        my_list.insert((my_list.index(number) + my_list.count(number)), number)
    if number not in my_list:
        my_list.append(number)
        my_list.sort(reverse=True)

    print(my_list)
    answer = input('Если хотите ввести новое число, введите yes: ')