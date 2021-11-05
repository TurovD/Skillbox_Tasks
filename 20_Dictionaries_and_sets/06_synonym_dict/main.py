
pair_dict = {}

for i in range(int(input('Введите количество пар слов: '))):
    first_word, second_word = input('{} пара: '.format(i + 1)).title().split(' - ')
    pair_dict[first_word] = second_word
    pair_dict[second_word] = first_word
print()
while True:
    word = input('Введите слово: ').title()
    if word in pair_dict:
        print('Синоним: ', pair_dict[word])
        break
    else:
        print('Такого слова в словаре нет.')