
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



def replace_item(site, key, replace_value):
    for keys, values in site.items():
        if isinstance(values, dict):
            site[keys] = replace_item(values, key, replace_value)
    if key in site:
        site[key] = replace_value
    return site


for _ in range(int(input('Сколько сайтов: '))):
    name = input('Введите название продукта для нового сайта: ')
    print('\nСайт для {}: '.format(name))
    replace_item(site,'title', 'Куплю/продам {} недорого'.format(name))
    replace_item(site, 'h2', 'У нас самая низкая цена на {}'.format(name))
    print (site)