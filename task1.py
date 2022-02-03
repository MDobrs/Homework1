from sys import argv

work_hour, per_hour, bonus = argv

print("Кол-во рабочих часов: ", work_hour)
print("Ставка в час: ", per_hour)
print("Премия: ", argv)
print("Заработная плата сотрудника: ", (int(work_hour)*int(per_hour)) + int(bonus))
