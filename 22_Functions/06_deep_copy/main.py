
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
         }
    }
 }

def changing_func(site,tag,name):
    if site.keys() == tag:
        print(1)
    else:
        changing_func(site)



for _ in range(int(input('Сколько сайтов: '))):
    name = input('Введите название продукта для нового сайта: ')
    changing_func(site,'title', name)
    changing_func(site,'h2', name)
