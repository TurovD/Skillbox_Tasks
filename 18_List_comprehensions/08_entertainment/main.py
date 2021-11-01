
import random


N_number = int(input('Кол-во палок: '))
sticks = ['|'] * N_number
for i in range(1, int(input('Кол-во бросков: '))+1):
    print('Бросок ', i, '.', sep='', end=' ')
    for downed_stick in range(int(input('Сбиты палки с номера '))-1, int(input('по номер '))):
        sticks[downed_stick] = '.'

print('Результат: ',''.join(sticks))