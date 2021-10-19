shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Введите название детали: ')
count_detail,total_price = 0,0
for product in shop:
 if product[0] == detail:
  count_detail += product.count(detail)
  price = product[1]
  total_price  += price
print('Кол-во деталей - ',count_detail)
print('Общая стоимость - ', total_price)