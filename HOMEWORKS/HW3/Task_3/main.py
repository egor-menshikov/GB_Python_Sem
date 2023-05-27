# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность

letters = {'AEIOULNSTRАВЕИНОРСТ': 1,
           'DGДКЛМПУ': 2,
           'BCMPБГЁЬЯ': 3,
           'FHVWYЙЫ': 4,
           'KЖЗХЦЧ': 5,
           'JXШЭЮ': 8,
           'QZФЩЪ': 10}

word = input('Введите любое слово:\n')
points = 0

for i in range(len(word)):
    for key, value in letters.items():
        if word[i].casefold() in key.casefold():
            points += value

print(f'{word} => {points} очка')
