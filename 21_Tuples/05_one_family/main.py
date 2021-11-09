family_dictionary = {
'Сидоров Никита': 35,
'Сидорова Алина': 34,
'Сидоров Павел': 10,
'Петров Александ': 32,
'Ургант Иван':43,
'Сталлоне Сильвестр': 75,
'Фёдоров Мирон ':36,
}

search = input('Кого ищем? ').title()
result = []
for name in family_dictionary:
    if search in name.split()[0].title(): result.append(name + ' '+str(family_dictionary[name]))

if not result: print('Поиск не дал результатов')
else:
    for name in result: print(name)