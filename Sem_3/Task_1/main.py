# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

from random import randint
list_1 = [randint(0, 10) for i in range(10)]
print(list_1)
print(set(list_1))
print(len(set(list_1)))