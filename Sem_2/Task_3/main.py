days = int(input('Введите количество дней:\n'))
streak = 0
answer = 0

for i in range(days):
    temp = int(input(f'Введите температуру в день {i+1}\n'))
    if temp > 0:
        streak += 1
    else:
        streak = 0
    if answer < streak:
        answer = streak

print(f'Оттепель длилась {answer} дней')