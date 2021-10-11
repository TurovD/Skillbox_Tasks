def min_divider(number, divider=2):
    if number % divider == 0:
        print('Наименьший делитель, отличный от единицы: ', divider)
    else:
        min_divider(number, divider + 1)

number = int(input('Введите число: '))
min_divider(number)