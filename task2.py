# 1 вариант 2-й задачи
def my_func(**kwargs):
    return kwargs


print(my_func(name=input("Введите имя: "),
              surname=input("Введите фамилию: "),
              birth=input("Введите год рождения: "),
              city=input("Введите город проживания: "),
              email=input("Введите электронку: "),
              phone=input("Введите номер телефона: ")))
