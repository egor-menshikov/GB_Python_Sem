# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

from random import randint
list_1 = []
for i in range(20):
    list_1.append(randint(0, 10))
q = set(list_1)
print(list_1)
print(q)
print(len(q))