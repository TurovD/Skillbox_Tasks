def sorting(elements):
    for element in elements:
        if not isinstance(elements, int):
            return elements
    return tuple(sorted(elements))


list_numbers = []
counts_number = int(input('Сколько элементов хотите добавить к кортеж? '))
control = True
for i in range(counts_number):
    new_element = input('Введите {} элемент: '.format(i+1))
    if new_element.isalpha():
        list_numbers.append(new_element)
        control = False
    elif float(new_element).is_integer():
        list_numbers.append(int(new_element))
    else:
        list_numbers.append(float(new_element))
        control = False
tuple_numbers = tuple(list_numbers)
if control is True:
    print('\nОтсортированный кортеж: ',sorting(tuple_numbers ))
else:
    print('\nХотя бы один элемент не является целым числом,исходный кортеж: ', sorting(tuple_numbers))
