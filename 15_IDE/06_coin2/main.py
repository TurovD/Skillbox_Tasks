def coin(coins_x,coins_y,r):
    if (abs(coins_x) <= r) and (abs(coins_y) <= r) :
        print('\nМонетка где-то рядом')
    else:
        print('\nМонетки в области нет')

coin(float(input('Введите координаты монетки \nX: ')),float(input('Y: ')),float(input('Введите радиус: ')))