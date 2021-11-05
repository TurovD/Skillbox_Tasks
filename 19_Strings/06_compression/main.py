text = input('Введите строку: ')
code_text = ''
for letter in text:
    if not len(code_text):
        code_text = letter + '1'
    else:
        if letter == code_text[-2]:
            code_text = '{}{}'.format(code_text[:-1], int(code_text[-1]) + 1)
        else:
            code_text = '{}{}{}'.format(code_text, letter, '1')
print(code_text)