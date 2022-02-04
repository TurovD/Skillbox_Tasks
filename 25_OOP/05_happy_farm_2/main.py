class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
            self.print_state()

    def is_ripe(self):
        if self.state == 3:
            self.state = 0
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        if True:
            for i_potato in self.potatoes:
                i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if not i_potato.is_ripe():
                print('\nКартошка ещё не созрела!')
            else:
                print('Вся картошка созрела! Можно собирать!\n')




class Gardener:
    gardener_name = input('Введите имя садовника: ')
    gardener_bed = input('Грядка с растением за которым ухаживает садовник: ')
    states_of_care = { 0: 'Сажает', 1: 'Удобряет', 2: 'Подкармливает', 3: 'Собирает и сажает' }

    def __init__(self):
        self.state_of_care = 0
        self.count_potato = []

    def print_state_of_care(self):
        print('\nСадовник сейчас {} картошку.'.format(
        Gardener.states_of_care[self.state_of_care]
        ))

    def harvest(self,count):
        for potato in range(count):
            self.count_potato.append(1)
        print('Садовник по имени {} собрал '.format(self.gardener_name),len(self.count_potato), ' шт. c грядок где растет {}.'.format( self.gardener_bed))


    def take_care_of_the_garden(self, count):
        if self.state_of_care < 3:
            self.state_of_care += 1
            self.print_state_of_care()
        if self.state_of_care == 3:
            my_garden.are_all_ripe()
            self.harvest(5)
            self.state_of_care = 0


my_garden = PotatoGarden(5)
g = Gardener()
g.print_state_of_care()
for _ in range(6):
    my_garden.grow_all()
    g.take_care_of_the_garden(5)
