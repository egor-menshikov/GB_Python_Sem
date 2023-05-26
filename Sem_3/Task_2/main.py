# list_1 = list(range(10))
# print(list_1)
# k = int(input('На сколько элементов сдвинуть список?\n'))
# k = k % len(list_1)
# print(k)
# if k >= 0:
#     for i in range(k):
#         list_1.insert(0, list_1.pop())
# else:
#     for i in range(len(list_1) - k):
#         list_1.insert(0, list_1.pop())
# print(list_1)
#
#
# data = [int(i) for i in input("Введите числа: ").split()]
# step = int(input("Введите кол-во сдвигов: "))
# step = step % len(data)
# data = [data[i - step] for i in range(len(data))]
# print(data)
#
# data = [int(i) for i in input("Введите числа: ").split()]
# for i in range((-1) * len(data), 0, +1):
#     print(data[i], i)
