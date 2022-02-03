#1
from itertools import count

print("Итератор, генерирующий целые числа, начиная с указанного")
n = int(input("Введите целое число:"))

for i in count(n):
    print(i, end=' ')

#2
from itertools import cycle

list = [5, 3, 3, 1, 0, 4, 2, 4, 7, 3]
for i in cycle(list):
    print(i, end=' ')