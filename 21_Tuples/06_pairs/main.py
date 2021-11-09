
first_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Оригинальный список: {} '.format(first_list))
new_dict = dict()
for i_index, i_value in enumerate(first_list):
    if i_index % 2 == 0:
        new_dict[i_index] = i_value

new_list = [(i_key, i_value + 1) for i_key, i_value in new_dict.items()]
print('Новый список: {}'.format(new_list))

# или
#first_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#print([*map(tuple, zip(first_list[::2], first_list[1::2]))])