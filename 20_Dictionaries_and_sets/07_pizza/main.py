count_order = int(input('Введите кол-во заказов: '))
dict_pizza = {}
for count in range(count_order):
    order = input('{} заказ: '.format(count + 1))
    client, pizza, amount = order.split(' ')
    amount = int(amount)
    if client not in dict_pizza:
        dict_pizza[client] = {pizza: amount}
    else:
        if pizza not in dict_pizza[client]:
            dict_pizza[client].update({pizza: amount})
        else:
            dict_pizza[client][pizza] += amount
for client, order in sorted(dict_pizza.items()):
    print(f'{client}:')
    for pizza, amount in sorted(order.items()):
        print('     {}: {}'.format(pizza, amount))
