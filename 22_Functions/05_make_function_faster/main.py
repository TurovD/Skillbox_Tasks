def calculating_math_func(data):
    if data in list_of_factorials:
        result = list_of_factorials[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        list_of_factorials[data] = result
    result /= data ** 3
    result = result ** 10
    return result


list_of_factorials = {}
for i in range (1, int(input('Сколько чисел вы хотите ввести? '))+1):
    print('Получившиеся число: ', calculating_math_func(int(input('\nВведите {} число: '.format(i)))))
