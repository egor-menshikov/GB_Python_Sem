# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8

limit = int(input('Введите число: \n'))
i = 0
power = 2 ** i

while power <= limit:
    print(power, end=' ')
    power *= 2
