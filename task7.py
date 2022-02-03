from math import factorial

def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)

print("Факториал числа: ")
for el in factorial_gen(8):
    print(el)
