# TODO здесь писать код
cages = int(input('Введите количество клеток: '))
list_cages = []
list_effectiveness = []
for i in range(1, cages+1):
    print('Эффективность',i,'клетки: ',end='')
    list_cages.append(input())
for effectiveness in range(len(list_cages)):
    if effectiveness > int(list_cages[effectiveness]):
        list_effectiveness.append(list_cages[effectiveness])
print('Неподходящие значения: ', *list_effectiveness, sep =' ')
