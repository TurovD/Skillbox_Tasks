
message = input('Сообщение: ')
special_symbol = True
new_word = ''
result = ''
for elements in message:
    if elements.isalpha():
        special_symbol = False
        new_word += elements
    elif not elements.isalpha() and special_symbol:
        result += elements
    elif not elements.isalpha() and not special_symbol:
        new_word = new_word[::-1]
        result += new_word
        result += elements
        new_word = ''
if new_word != '':
    new_word = new_word[::-1]
    result += new_word
print('Новое сообщение: ', result)