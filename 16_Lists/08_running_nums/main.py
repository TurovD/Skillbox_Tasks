# TODO здесь писать код
shift = int(input('Сдвиг: '))
first_list = [int(i) for i in input('Введите числа для изначального списка через пробел: ').split()]
final_list = first_list[-shift:] + first_list[:-shift]
print('\nИзначальный список: ',first_list)
print('Сдвинутый список: ',final_list)