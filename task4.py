def my_func(x, y):
    while True:
        try:
            x = float(x)
            y = int(y)
        except ValueError:
            print("Число не соответствует условию задачи. Попробуйте снова: ")
        if x < 0 and y > 0:
            print("Первое число должно быть положительным, второе - отрицательным: ")
            break
        else:
            return x ** y


a = (input("Введите число: "))
b = (input("Введите число: "))
print(my_func(a, b))