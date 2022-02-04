class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            None

class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            None

class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Vapor()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            None

class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            None

class Storm:
    def __str__(self):
        return 'Шторм'

class Vapor:
    def __str__(self):
        return 'Пар'

class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'

class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


def main():
    water = Water()
    air = Air()
    earth = Earth()
    fire = Fire()
    print(f'{water} + {air}\n'
    f'Abracadabra, genie-in-a-bottle kind of way.... \n'
    f'Получается: { water + air }\n'
    f'\n{water} + {fire}'
    f'\nAbracadabra, genie-in-a-bottle kind of way.... \n'
    f'Получается: { water + fire }\n '
    f'\n{water} + {earth}'
    f'\nAbracadabra, genie-in-a-bottle kind of way.... \n'
    f'Получается: { water + earth }\n'
    f'\n{air} + {fire}'
    f'\nAbracadabra, genie-in-a-bottle kind of way.... \n'
    f'Получается: { (air + fire)}\n '
    f'\n{air} + {earth}'
    f'\nAbracadabra, genie-in-a-bottle kind of way.... \n'
    f'Получается: { (air + earth)}\n '
    f'\n{earth} + {fire}'
    f'\nAbracadabra, genie-in-a-bottle kind of way.... \n'
    f'Получается: { (earth + fire)}\n ')

if __name__ == '__main__':
    main()
