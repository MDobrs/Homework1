with open("trial1.txt.", "r", encoding="utf-8") as t_1:
    content = t_1.readlines()
    lines = len(content)
    print(f"Строк {lines}")
    l = 0
    for i in content:
        words = i.split(" ")
        words = len(words)
        l += 1
        print(f"Слов в {l} строке - {words}")