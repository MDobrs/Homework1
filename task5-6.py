costs = int(input("Введите издержки: "))
income = int(input("Введите прибыль: "))
if costs > income:
    print("Фирма работает с убытком")
if costs < income:
    print("Фирма работает с прибылью")
    profit = income - costs
    people = int(input("Введите число сотрудников: "))
    per_capita = profit/people
    print("Прибыль в расчете на сотрудника составляет {}".format(per_capita))
if costs == income:
    print("Фирма на самоокупаемости")
