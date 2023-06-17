from data_create import name_data, surname_data, phone_data, address_data
import json

PATH = 'phonebook.json'


def print_data():
    with open(PATH, 'r', encoding='utf-8') as file:
        phonebook = json.load(file)
    print()
    for k, v in phonebook.items():
        print(f'{k:^2} {v["name"]:<12} {v["surname"]:<14} {v["phone"]:<16} {v["address"]:<16}')
    return phonebook


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


def edit_data():
    phonebook = print_data()

    print(contact_choice := input('Введите номер записи, которую вы хотите изменить: '))
    while True:
        if contact_choice.isdigit() and 0 < int(contact_choice) <= len(phonebook):
            print(f'\nВы хотите изменить:\n\n'
                  f'{phonebook[contact_choice]["name"]:<12}'
                  f' {phonebook[contact_choice]["surname"]:<14}'
                  f' {phonebook[contact_choice]["phone"]:<16}'
                  f' {phonebook[contact_choice]["address"]:<16}')
            break
        else:
            print(contact_choice := input('Введите номер записи, которую вы хотите изменить: '))
    print(f'{"1) Имя":<12}'
          f' {"2) Фамилия":<14}'
          f' {"3) Телефон":<16}'
          f' {"4) Адрес":<16}')

    print(column_choice := int(input('\nВыберите соответствующую категорию: ')))
    while True:
        match column_choice:
            case 1:
                phonebook[contact_choice]["name"] = name_data()
                break
            case 2:
                phonebook[contact_choice]["surname"] = surname_data()
                break
            case 3:
                phonebook[contact_choice]["phone"] = phone_data()
                break
            case 4:
                phonebook[contact_choice]["address"] = address_data()
                break
            case _:
                print(column_choice := int(input('\nВыберите соответствующую категорию: ')))

    with open(PATH, 'w', encoding='utf-8') as file:
        json.dump(phonebook, file, ensure_ascii=False)


def delete_data():
    phonebook = print_data()
    print(contact_choice := input('Введите номер записи, которую вы хотите удалить: '))
    phonebook.pop(contact_choice)
    contact_list = [v for k, v in phonebook.items()]
    phonebook = {str(k): v for k, v in enumerate(contact_list, 1)}
    with open(PATH, 'w', encoding='utf-8') as file:
        json.dump(phonebook, file, ensure_ascii=False)


def search_data():
    with open(PATH, 'r', encoding='utf-8') as file:
        phonebook = json.load(file)
    print(prompt := input('\nЧто вы хотите найти?\n-> ').casefold())
    for k, v in phonebook.items():
        for value in v.values():
            if value.find(prompt) != -1:
                print(f'{k:^2} {v["name"]:<12} {v["surname"]:<14} {v["phone"]:<16} {v["address"]:<16}')
                break

# delete_data()
# input_data()
# edit_data()
# print_data()
# search_data()
