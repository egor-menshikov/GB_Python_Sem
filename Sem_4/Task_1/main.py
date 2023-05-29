# Напишите программу, которая принимает на вход строку, и отслеживает, сколько
# раз каждый символ уже встречался. Количество повторов добавляется к символам
# с помощью постфикса формата _n.
#
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

word = input("Введите текст: ")
word_ = [i for i in word]
print((word_))

# Решение препода
# word = input("Введите текст: ").split()
# result = {}
# for i in word:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#         result[i] += 1
#     else: # ключа i нет внутри словаря result
#         print(i, end=' ')
#         result[i] = 1

# второе решение
# word = input("Введите текст: ").split()
# result = {}
# for i in word:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else: # ключа i нет внутри словаря result
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1