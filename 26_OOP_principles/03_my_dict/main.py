class Mydict(dict):
    def get(self, key, default = 0):
        return dict.get(self, key, default)

dictionari = Mydict(a = 1, b = 2, c = 3, d = 4, f = 5)

print('Словарь состоит из :',dictionari )
symbol = input('Какой символ нужно найти? ')
print('Поиск символа {} в словаре: '.format(symbol),dictionari.get(symbol))