# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику...
from random import randint

list_ = [randint(1, 33) for i in range(int(input('Введите количество кустов: ')))]
sums = []
for i in range(len(list_)):
    sums.append(list_[(i - len(list_) - 1) % len(list_)] +
                list_[(i - len(list_)) % len(list_)] +
                list_[(i - len(list_) + 1) % len(list_)])

print('Кусты:')
print(list_)
print('Суммы групп ягод по "центральному" кусту:')
print(sums)
print(f'Максимум ягод {max(sums)} можно собрать если остановиться у {sums.index(max(sums)) + 1} куста')