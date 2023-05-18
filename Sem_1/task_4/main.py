n = int(input("Введите год\n"))

if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print(f'Год {n} високосный')
else:
    print(f'Год {n} не високосный')