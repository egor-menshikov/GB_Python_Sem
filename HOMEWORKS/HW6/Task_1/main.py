# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.


def progression(first_elem: int, diff: int, elem_count: int) -> list[int]:
    return [first_elem + i for i in range(0, elem_count * diff, diff)]


_, __, ___ = [int(i) for i in input('Введите условия прогрессии через пробел:\n').split()]
print(progression(_, __, ___))
