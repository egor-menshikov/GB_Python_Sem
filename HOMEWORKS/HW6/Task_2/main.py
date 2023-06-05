# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
from random import randint


def range_idx(min_: int, max_: int, array: list[int]) -> list[int]:
    return [i for i in range(len(array)) if min_ <= array[i] <= max_]


list_ = [randint(-20, 20) for i in range(20)]
print(list_)
range_min = int(input('Введите нижнюю границу диапозона: '))
range_max = int(input('Введите верхнюю границу диапозона: '))
print('Индексы найденных элементов:')
print(range_idx(range_min, range_max, list_))
