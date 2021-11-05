
text = input('Введите строку: ').split()
biggest_word = (max(text, key=len))
len_word = len(biggest_word)
print('Самое длинное слово:', biggest_word)
print('Длина слова:', len_word, 'букв')