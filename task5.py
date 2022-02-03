from functools import reduce

items = list(range(100, 1001, 2))
count_all = reduce(lambda x, y: x * y, items)
print(count_all)