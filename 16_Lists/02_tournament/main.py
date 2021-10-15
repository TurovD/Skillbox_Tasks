#Человек с чётным индексом.
# names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
# list_second_names = names_list[::2]
# for i in range(len(list_second_names)):
#     print(list_second_names[i],end=' ')

#Каждый второй из списка.
names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
for i in range(1,len(names_list), 2):
     print(names_list[i], end=' ')