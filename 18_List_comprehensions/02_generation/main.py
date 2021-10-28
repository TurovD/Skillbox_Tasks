


number_list = list([(1 if number % 2 == 0 else number % 5) for number
                    in range(int(input('Введите длину списка: ')))])
print('Результат: ',number_list)