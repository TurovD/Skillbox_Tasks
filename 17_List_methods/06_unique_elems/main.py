first_list = [int(i) for i in input('Введите 3 числа для первого списка через пробел: ').split()]
second_list = [int(num) for num in input('Введите 7 чисел для второго списка через пробел: ').split()]
print('\nПервый список: ',first_list)
print('Второй список: ',second_list)
second_list.reverse()
first_list.extend(second_list)
print(first_list)
first_list = list(dict.fromkeys(first_list))
first_list.reverse()
print('\nНовый первый список с уникальными элементами: ', first_list)