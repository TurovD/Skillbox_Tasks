a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
digits_five = a.count(5)
print('Кол-во цифр 5 при первом объединении: ', digits_five)
for _ in range(digits_five):
    a.remove(5)
a.extend(c)
digits_three = a.count(3)
print('Кол-во цифр 3 при втором объединении: ',digits_three )
print(a)