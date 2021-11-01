number_list = [int(number) for number in input('Введите элементы массива через пробел: ').split()]
list_without_zero = [num for num in number_list if num !=0 ]
list_zero = [num for num in number_list if num==0]
new_number_list = list_without_zero + list_zero
print('\nОтсортированный список: ',new_number_list)
new_number_list = list_without_zero
print('\nСжатый список: ',new_number_list)