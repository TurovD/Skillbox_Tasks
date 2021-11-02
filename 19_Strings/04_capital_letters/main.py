text = input('Введите строку: ')
upper_first_letter = ' '.join(letter[0].upper() + letter[1:] for letter in text.split())
print(upper_first_letter)