stroka = str(input("Введите строку любой длины с любым количеством слов"))
n = (stroka.split())
counter=0
for i in n:
    counter+=1
    if len(i)<=10:
        print(counter,' ', i)
    if len(i)>10:
        print(counter,' ', i[0:10])