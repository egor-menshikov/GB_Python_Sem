# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A. Последняя строка содержит число X.

from random import randint

list_length = int(input('Введите длину массива: '))
data = [randint(-10, 10) for i in range(list_length)]
# data = [4, 1, 3, 6, 32, 6, 4]
print(data)
num_x = int(input('Введите число: '))

abs_diff = [abs(num_x - item) for item in data]
indexes = [idx for idx, value in enumerate(abs_diff) if value == min(abs_diff)]
values = [data[value] for value in indexes]

print(f'{abs_diff} <== Разность по модулю между нашим числом и элементами списка')
print(f'{indexes}  <== Индексы наиболее близких по значению элементов')
print(f'{values}  <== Значения')

