
plenty_finish = set(range(1, int(input('Введите максимальное число: ')) + 1))
while (choose := input('\nНужное число есть среди этих чисел: ')).title() != 'Помогите!':
    selected_number = set(map(int, choose.split()))
    quest = input('Ответ Артёма: ').title()
    if quest == 'Да':
        plenty_finish &= selected_number
    else:
        plenty_finish -= selected_number
print('Артём мог загадать следующие числа: ', *plenty_finish )




