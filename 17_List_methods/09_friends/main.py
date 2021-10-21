freinds = int(input('Кол-во друзей: '))
credit_count = int(input('Кол-во долговых расписок: '))
freinds_credit_list = []
for _ in range(freinds):
    freinds_credit_list.append(0)

for counts in range(1,credit_count+1):
    print('\nРасписка под номером',counts)
    to_freind = int(input('Кому: '))
    from_freind = int(input('От кого: '))
    credit_size = int(input('Сколько: '))
    freinds_credit_list[from_freind-1] += credit_size
    freinds_credit_list[to_freind-1] -= credit_size
print('Баланс друзей: ')
for index in range(len(freinds_credit_list)):
    print(index+1, ':', freinds_credit_list[index])