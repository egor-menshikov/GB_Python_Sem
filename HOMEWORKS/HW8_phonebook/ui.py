from logger import input_data, print_data, edit_data, delete_data, search_data


def print_menu():
    print('\nМеню:\n'
          '1. Добавить контакт\n'
          '2. Удалить контакт\n'
          '3. Редактировать контакт\n'
          '4. Вывести данные\n'
          '5. Поиск контакта\n'
          '6. Выход')


def interface():
    command = -1
    while command != 6:
        print_menu()
        command = int(input("Введите номер операции: "))

        while command < 1 or command > 6:
            print('Вы ошиблись при выборе.')
            command = int(input("Введите номер операции: "))

        if command == 1:
            input_data()
        elif command == 2:
            delete_data()
        elif command == 3:
            edit_data()
        elif command == 4:
            print_data()
        elif command == 5:
            search_data()
        elif command == 6:
            print("Всего доброго!")
