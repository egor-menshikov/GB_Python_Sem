# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input('Enter a 3-digit number:\n'))

answer = num // 100 + num // 10 % 10 + num % 10

print(f'The sum of digits in:\n {num} -> {answer}')