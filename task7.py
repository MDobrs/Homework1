a = int(input())
b = int(input())
counter = 0
while a < b:
    n = (((a*10)/100)+a)
    counter += 1
    print("{}-й день: {}".format(counter, n))
    a = n
print("На {}-й день спортсмен достиг результата — не менее 3 км.".format(counter))