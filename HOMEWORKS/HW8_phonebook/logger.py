from data_create import name_data, surname_data, phone_data, address_data
import json

PATH = 'phonebook.json'


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    contact = {'name': name, 'surname': surname, 'phone': phone, 'address': address}

    with open(PATH, 'r', encoding='utf-8') as file:
        phonebook = json.load(file)
    for i in range(1, len(phonebook) + 2):
        if str(i) not in phonebook.keys():
            phonebook[i] = contact
            break
    with open(PATH, 'w', encoding='utf-8') as file:
        json.dump(phonebook, file, ensure_ascii=False)


def print_data():
    with open(PATH, 'r', encoding='utf-8') as file:
        phonebook = json.load(file)
    for k, v in phonebook.items():
        print(f'{k:^2} {v["name"]:<12} {v["surname"]:<14} {v["phone"]:<16} {v["address"]:<16}')


def edit_data():
    with open(PATH, 'r', encoding='utf-8') as file:
        phonebook = json.load(file)
        for k, v in phonebook.items():
            print(f'{k:^2} {v["name"]:<12} {v["surname"]:<14} {v["phone"]:<16} {v["address"]:<16}')
        print(contact_choice := input('Введите номер записи, которую вы хотите изменить: '))
        print(f'\nВы хотите изменить:\n\n'
              f'{phonebook[contact_choice]["name"]:<12}'
              f' {phonebook[contact_choice]["surname"]:<14}'
              f' {phonebook[contact_choice]["phone"]:<16}'
              f' {phonebook[contact_choice]["address"]:<16}')
        print(f'{"1) Имя":<12}'
              f' {"2) Фамилия":<14}'
              f' {"3) Телефон":<16}'
              f' {"4) Адрес":<16}')
        print(column_choice := int(input('\nВыберите соответсвующую категорию: ')))
        match column_choice:
            case 1:
                print('Введите новое имя: ')
                phonebook[contact_choice]["name"] = input()
            case 2:
                print('Введите новую фамилию: ')
                phonebook[contact_choice]["surname"] = input()
            case 3:
                print('Введите новый телефон: ')
                phonebook[contact_choice]["phone"] = input()
            case 4:
                print('Введите новый адрес: ')
                phonebook[contact_choice]["address"] = input()
    with open(PATH, 'w', encoding='utf-8') as file:
        json.dump(phonebook, file, ensure_ascii=False)


def delete_data():
    with open(PATH, 'r', encoding='utf-8') as file:
        phonebook = json.load(file)
    for k, v in phonebook.items():
        print(f'{k:^2} {v["name"]:<12} {v["surname"]:<14} {v["phone"]:<16} {v["address"]:<16}')
    print(contact_choice := input('Введите номер записи, которую вы хотите удалить: '))
    phonebook.pop(contact_choice)
    contact_list = [v for k, v in phonebook.items()]
    phonebook = {str(k): v for k, v in enumerate(contact_list, 1)}
    with open(PATH, 'w', encoding='utf-8') as file:
        json.dump(phonebook, file, ensure_ascii=False)

# delete_data()
# input_data()
# edit_data()
# print_data()
