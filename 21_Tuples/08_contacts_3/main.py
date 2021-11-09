def search_man():
    search = input('Кого ищем? ').title()
    result = []
    for name in family_dictionary:
        if search in name.split()[0].title():
            result.append(name + ' ' + str(family_dictionary[name]))
    if not result:
        print('Поиск не дал результатов')
    else:
        for name in result: print(name)

def phone_number():
    dict_name = {name: int(input('Введите номер телефона нового контакта:'))}
    family_dictionary.update(dict_name)
    dict_name.clear()
    print('Текущий список контактов выглядит так: ', family_dictionary)



family_dictionary = {
'Сидоров Никита': 89120487544,
'Сидорова Алина': 89120424544,
'Сидоров Павел': 89120489544,
'Петров Александ': 89120127544,
'Ургант Иван':89120947544,
'Сталлоне Сильвестр': 89120325454,
'Фёдоров Мирон ':89020447544,
}


while True:
    action = input('\nВведите действие ("Добавить контакт" или "Поиск человека по фамилии", чтобы закончить введите "Стоп": ').title()
    result = []
    if action == 'Добавить Контакт':
        name = input('Введите Фамилию и Имя нового контакта: ').title()
        if name in family_dictionary:
            print('Такой человек уже есть в телефонной книге.')
            qust = input('Чтобы обновить номер введите "Обновить",если хотите ввести новое имя введите любой символ: ').title()
            if qust == 'Обновить':
                phone_number()
        if name not in family_dictionary:
            phone_number()
    elif action == 'Поиск Человека По Фамилии':
        search_man()
    if action == 'Стоп':
        print('Хорошего дня!')
        break