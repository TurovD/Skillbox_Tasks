with open('numbers.txt') as datfile:
    text = datfile.read()
print("Содержимое файла answer.txt\n", sum(map(int, text.split(None))))
