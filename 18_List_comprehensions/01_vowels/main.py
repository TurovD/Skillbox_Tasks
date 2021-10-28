letters = ['у','ё','е','э','о','а','ы','я','и','ю','У','Ё','Э','О','А','Ы','Я','И','Ю']
text = list(input('Введите текст: '))
vowel_list = list([vowel for vowel in text if vowel in letters])
print('Список гласных букв: ',vowel_list,
      '\nДлина списка: ',len(vowel_list))
