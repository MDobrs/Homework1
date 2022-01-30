def int_func(text):
    return text.capitalize()


line = input("Введите строку: ")
n = (line.split())
for i in n:
    print(int_func(i), end=" ")