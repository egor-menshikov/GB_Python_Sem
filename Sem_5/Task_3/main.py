# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

# def prime_check(num):
#     for i in range(num//2, 1, -1):
#         if num % i == 0:
#             return False
#         return True
#
# our_num = int(input('Ввведите число:\n'))
# print(prime_check(our_num))


def IsPrime(n):
   for i in range(2, n // 2 + 1):
      if n % i == 0:
         return 'no'
   return 'yes'


n = int(input())
print(IsPrime(n))