
def summ_number(number):
    summ = 0
    while number > 0:
        digit = number % 10
        summ += digit
        number //= 10
    print('\nСумма цифр: ', summ)
    return(summ)

def count_number(number):
    count = number
    digit_number = 0
    while count > 0:
        digit_number += 1
        count //= 10
    print('Кол-во цифр в числе: ', digit_number)
    return(digit_number)

def difference_number(number):
    difference = summ_number(number) - count_number(number)
    print('Разность суммы и кол-ва цифр: ', difference)

def main_menu():
    number = int(input('Введите целое положительное число: '))
    difference_number(number)

main_menu()