def score(result):
    return result[1][0] - result[1][1]

score_table = { }
number_players = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя): ')
for count in range(number_players):
    points, name = input('{} запись: '.format(count + 1)).split()
    points = int(points)
    if name in score_table:
        if points > score_table[name][0]:
            score_table[name][0] = points
            score_table[name][1] = count
    else:
        score_table[name] = [points, count]
scores = list(score_table.items())

scores.sort(key=score ,reverse=True)
print('\nИтоги соревнований: ')
for winner_index in 0, 1, 2:
    print(f' { winner_index + 1 } место { scores[winner_index][0] } ', end=' ')
    print(f'( { scores[winner_index][1][0] } )', sep='')

