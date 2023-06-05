# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

def prime_check(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return 'no'
    return 'yes'


n = int(input())
print(prime_check(n))
