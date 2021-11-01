number_num = int(input('Введите кол-во чисел: '))
number_list = []
for i in range(number_num):
    number_list.append(int(input('Число: ')))
print('\nПоследовательность: ',*number_list)
count_number = 0
while number_list != number_list[::-1]:
    number_list.insert(number_num, number_list[count_number])
    count_number += 1
print('Нужно дописать чисел: ',count_number)
print('Сами числа: ',*number_list[:count_number][::-1])