def super_functional(input_tuple, element):
    if element in input_tuple:
        if input_tuple.count(element) > 1:
            first_index = input_tuple.index(element)
            second_index = input_tuple.index(element, first_index + 1) + 1
            return input_tuple[first_index:second_index]
        else:
            return input_tuple[input_tuple.index(element):]
    else:
        return ()

input_tuple = input('Введите кортеж, через запятую: ')
input_tuple = tuple(int(x) for x in input_tuple.split(","))
element = int(input('Введите элемент: '))
print('Результат: ',super_functional(input_tuple, element))