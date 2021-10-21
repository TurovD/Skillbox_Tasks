
def game():
    out = 0
    for _ in range(len(people_list) - 1):
        print('\nТекущий круг людей', people_list )
        start_count = out % len(people_list )
        out = (start_count + number - 1) % len(people_list )
        print('Начало счёта с номера', people_list [start_count])
        print('Выбывает человек под номером', people_list [out])
        people_list.remove(people_list[out])
    print('\nОстался человек под номером: ', people_list[0] )


people_count = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', number, 'человек')
people_list = list(range(1,people_count+1))
game()