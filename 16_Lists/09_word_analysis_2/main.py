# TODO здесь писать код
word = list(input('Введите слово: '))
compare_word = word[::-1]
if compare_word == word:
    print('\nСлово является палиндромом')
else:
    print('\nСлово не является палиндромом')