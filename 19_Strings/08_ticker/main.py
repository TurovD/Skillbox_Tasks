
def swap_string(first_string,second_string):
    if second_string == first_string:
        print('Вы ввели две одинаковые строки')
    else:
        count_swap = 1
        for i in range(len(second_string)):
            second_string = second_string[-1]+second_string[:-1]
            if second_string == first_string:
                control = True
                print('Первая строка получается из второй со сдвигом ', count_swap,'.')
                break
            else:
                count_swap +=1
                control = False
        if not control:
            print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


first_string = input('Первая строка: ')
second_string = input('Вторая строка: ')
swap_string(first_string,second_string)