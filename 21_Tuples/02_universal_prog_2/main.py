def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n ==0:
            return False
    return True


def programm_2(massif):
    result = []
    for i in range(len(massif)):
        if is_prime(i) is True:
            result.append(massif[i])
    return result

choice = input('Какой итерируемый объект будет? (котреж, строка, список, словарь): ').title()
if choice =='Список':
    massif  = input('Введите список, через запятую: ')
    massif  = list(int(x) for x in massif.split(","))
if choice == 'Кортеж':
    massif = input('Введите Кортеж, через запятую: ')
    massif = tuple(int(x) for x in massif.split(","))
if choice =='Строка':
    massif  = input('Введите строчку: ')
if choice =='Словарь':
    dictionary = {}
    length = int(input("Введите длину словаря: "))
    for element in range(0, length):
        dictionary[int(input('Введите ключ: '))] = input('Введите значение: ')
    print(dictionary)
    massif = dictionary

print(programm_2(massif))

