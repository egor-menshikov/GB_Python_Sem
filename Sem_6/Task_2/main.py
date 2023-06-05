# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел

from random import randint


def big_elems(list_: list[int]) -> int:
    count = 0
    for i in range(1, len(list_) - 1):
        if list_[i - 1] < list_[i] > list_[i + 1]:
            count += 1
    return count


our_list = [randint(1, 7) for i in range(10)]
print(our_list)
print(big_elems(our_list))


# n = int(input())
# list_1 = [int(i) for i in input().split()][:n]
# print(sum([int(list_1[i - 1] < list_1[i] > list_1[i + 1]) for i in range(1, n - 1)]))
