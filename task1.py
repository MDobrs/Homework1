with open("trial1.txt.", "w", encoding="utf-8") as t_1:
    enter = input("Введите строку:")
    while enter != "":
        to_file = t_1.writelines([str(enter), "\n"])
        enter = input("Введите строку:")

