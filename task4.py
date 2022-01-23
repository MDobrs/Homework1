num = int(input("Введите число"))
max_digit = 0
while num > 0:
    cur_digit = num % 10
        if cur_digit > max_digit:
            max_digit = cur_digit
        num = num//10


print(max_digit)