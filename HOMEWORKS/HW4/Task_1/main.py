# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

list_1 = [randint(0, 9) for i in range(int(input('Введите длину первого списка: ')))]
list_2 = [randint(0, 9) for i in range(int(input('Введите длину второго списка: ')))]
print(list_1)
print(list_2)
print(sorted(set(list_1).intersection(set(list_2))))
