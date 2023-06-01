from random import randint


def min_grades(list_):
    for i in range(len(list_)):
        if list_[i] == max(list_):
            list_[i] = min(list_)

num = int(input('Введите количество записей журнала:\n'))
grades = [randint(1, 5) for i in range(num)]
print(grades)
min_grades(grades)
print(grades)
