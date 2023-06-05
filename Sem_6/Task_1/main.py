# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

from random import randint


def list_diff(list_1: list[int], list_2: list[int]) -> list[int]:
    result = [list_1[i] for i in range(len(list_1)) if list_1[i] not in list_2]
    return result


l_1 = [randint(0, 10) for i in range(10)]
l_2 = [randint(0, 10) for i in range(10)]

print(l_1)
print(l_2)
print(list_diff(l_1, l_2))
