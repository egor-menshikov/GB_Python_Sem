# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.


def same_by(char, obj):
    if len(set(list(map(char, obj)))) > 1:
        return False
    else:
        return True


values = [0, 2, 10, 6, 13]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')