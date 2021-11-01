import random

first_team = [round(random.uniform(5, 10), 2) for num in range(20)]
second_team = [round(random.uniform(5, 10), 2) for num in range(20)]
winers = [max(num) for num in zip(first_team,second_team)]
print ('Первая команда: ', first_team)
print ('Вторая команда: ', second_team)
print('Победители тура: ',winers)