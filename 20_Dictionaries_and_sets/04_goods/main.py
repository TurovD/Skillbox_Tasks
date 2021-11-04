goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product_title, product_code in goods.items():
    product_total_quantity = 0
    product_total_cost = 0
    for product in store[product_code]:
        product_quantity = 0
        product_cost = 0
        product_quantity += product['quantity']
        product_cost += product['price']
        product_total_cost += product_quantity * product_cost
        product_total_quantity += product_quantity
    print('{0} - {1} шт, стоимость {2} руб.'.format(product_title, product_total_quantity, product_total_cost))


