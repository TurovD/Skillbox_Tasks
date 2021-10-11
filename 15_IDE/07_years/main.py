def years(start,finish):
    answer = []
    for number in range(start,finish+1):
        string = str(number)
        multitude = set(string)
        for symbol in multitude:
            if string.count(symbol) > 2:
                answer.append(number)
    print('Года от', start, 'до', finish,'с тремя одинаковыми цифрами: ')
    print(*answer,sep='\n')

years(int(input('Введите первый год: ')),int(input('Введите второй год: ')))