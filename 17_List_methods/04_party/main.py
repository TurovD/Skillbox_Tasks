guests, control = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя'],True


while True:
    print('\nСейчас на вечеринке',len(guests) ,'человек: ',guests)
    action_guest = input('Гость пришёл или ушёл, или пора спать? ')
    if action_guest == 'Пора спать' or action_guest == 'пора спать' or action_guest == 'пораспать':
        print('\nВечеринка закончилась, все легли спать.')
        break

    name_guest = input('Введите имя Гостя: ')
    if action_guest == 'пришел' or action_guest == 'пришёл' or action_guest == 'Пришёл' or action_guest == 'пришёл':
        if len(guests) < 6:
            guests.append(name_guest)
            print('Привет, ', name_guest, '!')
        else:
            print('Прости, ', name_guest, ', но мест нет.')
    elif action_guest == 'ушёл' or action_guest == 'ушел' or action_guest == 'Ушел' or action_guest == 'Ушёл':
        print('Пока, ', name_guest, '!')
        guests.remove(name_guest)