# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве
# аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число
# строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как,
# например, у операции умножения.

# print_operation_table(lambda x, y: x * y)

def print_operation_table(operation, num_rows=6, num_columns=6):
    list_ = []
    for i in range(0, num_rows):
        row_ = []
        for j in range(0, num_columns):
            row_.append(operation(i + 1, j + 1))
        list_.append(row_)
    # return print('\n'.join(map(str, list_)))
    return print(*list_, sep='\n')


print_operation_table(lambda x, y: x * y)
