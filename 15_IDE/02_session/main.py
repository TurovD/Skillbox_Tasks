# TODO здесь писать код
print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2
if x_diff == 0:
    k = 0
    print('Так как X2-X1=0, то уравнение прямой нельзя записать в каноническом виде.')
    print('\nДанная прямая параллельна оси OY, а её уравнение можно записать в виде: x =', x1)
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", k, " * x + ", b)
