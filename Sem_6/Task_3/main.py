# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.


list_ = [int(i) for i in input('Введите числа через пробел:\n').split()][:10]
print(list_)
dict_ = dict()

for item in list_:
    dict_[item] = list_.count(item) // 2
print(dict_)

# list_1 = [int(i) for i in input().split()]
# result = {}
# for element in list_1:
#     if element in result:
#         result[element] += 1
#     else:
#         result[element] = 1
# print(sum([i // 2 for i in result.values()]))
