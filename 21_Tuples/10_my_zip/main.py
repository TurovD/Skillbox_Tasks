


string_1 = input('Строка: ')
tuple_1 = tuple(input('Кортеж чисел (Введите через запятую): ').split(','))
print('\nРезультат:','\n<generator object <genexpr> at 0x00000204A4234048>')
for pair in ((string_1[i], tuple_1[i]) for i in range(min(len(string_1), len(tuple_1)))):
    print (pair)