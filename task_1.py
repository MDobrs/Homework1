def division(arg1, arg2):
    try:
        return arg1 / arg2
    except ZeroDivisionError:
        print("Деление на ноль невозможно")


a = int(input("Введите число: "))
b = int(input("Введите число: "))

print(division(a, b))
