def recursion(num):
    if num >= 1:
        recursion(num - 1)
        print(num,end=' ')


recursion(int(input('Введите число: ')))