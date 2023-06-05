# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def num_power(a, b):
    if b == 0:
        return 1
    return a * num_power(a, b - 1)

num = int(input('Введите число:\n'))
power = int(input('Введите степень:\n'))
print(num_power(num, power))
