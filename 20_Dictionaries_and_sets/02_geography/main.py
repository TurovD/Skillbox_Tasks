set_countries = {}
for count_country in range(0, int(input('Кол-во стран: '))):
    value = input('{} страна: '.format(count_country+1)).split()
    for city_set in value[1:]:
        set_countries[city_set] = value[0]
for count in range(1, 4):
    city = input('\n{} город: '.format(count))
    country = set_countries.get(city)
    if country:
        print('Город {} расположен в стране {}.'.format(city,country))
    else:
        print('По городу {} данных нет.'.format(city))