# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух
# считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы
# отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


def vowel_count():
    vowels = 'аеёиоуыэюя'
    text = input('Введите стихотворение: ').casefold().split()
    result = []
    for item in text:
        count = 0
        for vowel in item:
            if vowel in vowels:
                count += 1
        result.append(count)
    if min(result) == max(result):
        return print('Парам пам-пам')
    return print('Пам парам')


vowel_count()