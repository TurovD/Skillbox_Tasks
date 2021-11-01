def caesar(text, shift):
    alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ',
                'ы','ь','э','ю','я']
    shifted_text = ([' ' if i == ' ' else (alphabet[(alphabet.index(i)+shift)-33] if (alphabet.index(i)+shift)>32
                                            else alphabet[(alphabet.index(i)+shift)])  for i in text])
    print('Зашифрованное сообщение: ',''.join(shifted_text))

text = [letter for letter in input('Введите сообщение: ').lower()]
shift = int(input('Введите сдвиг: '))
caesar(text,shift)