
import collections

def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict

text = input('Введите текст: ')
hist = histogram(text)
print('Оригинальный словарь частот:')
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])


inverted_dictionary = dict()
for letter, number in collections.Counter(text).items():
    inverted_dictionary.setdefault(number, []).append(letter)
print('\nИнвертированный словарь частот: ')
for inverted in inverted_dictionary:
    print(inverted, ':', inverted_dictionary[inverted])