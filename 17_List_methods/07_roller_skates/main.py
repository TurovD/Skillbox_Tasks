skates = int(input('\nВведите кол-во коньков: '))
skates_list = []
count = 0
for s in range(1,skates+1):
    print('Введите размер',s,'человека: ',end='')
    skates_list.append(input())

legs = int(input('\nВведите кол-во людей: '))
legs_list = []
for l in range(1,legs+1):
    print('Введите размер',l,'человека: ',end='')
    legs_list.append(input())

for counts in legs_list:
    for j in range(len(skates_list)):
        if skates_list[j] >= counts:
            skates_list.remove(skates_list[j])
            count += 1
            break

print('\nНаибольшее кол-во людей, которые могут взять ролики: ',count)