text = input('Введите текст в котором h встречается как минимум два раза: ')
start = text.index('h')
finish = text.rindex('h')
print(text[:start+1] + text[finish-1:start:-1] + text[finish:])