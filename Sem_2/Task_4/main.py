num = int(input('Введите количество арбузов:\n'))
min = 1000
max = 0
for i in range(num):
    weight = int(input(f'Сколько весит арбуз {i+1}?\n'))
    if min > weight:
        min = weight
    if max < weight:
        max = weight

print(f'min = {min}\n max = {max}')