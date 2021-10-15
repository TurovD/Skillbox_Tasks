

cards = int(input('Введите количество видеокарт: '))
list_cards = []
for i in range(1, cards+1):
    print(i,'Видеокарта: ',end='')
    list_cards.append(int(input()))
print('Старый список видеокарт: ', list_cards, sep =' ')
new_cards_list = [card for card in list_cards if card!=max(list_cards)]
print('Новый список видеокарт: ', new_cards_list )
