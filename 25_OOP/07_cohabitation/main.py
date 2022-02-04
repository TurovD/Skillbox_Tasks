from random import randint

class House:
    food = 50
    money = 0

class Person:

    def __init__(self, name):
        self.name = name
        self.health = 50

    def eat(self):
        self.health += 1
        House.food -= 1
        return f' решил поесть. Уровень сытости: {self.health}; еды осталось {House.food} штук'

    def work(self):
        self.health -= 1
        House.money += 1
        return f'работает. Уровень сытости: {self.health}; денег осталось: {House.money} ден. ед.'

    def play_games(self):
        self.health -= 1
        return f'играет. Уровень сытости: {self.health}'

    def shoping(self):
        House.food += 1
        House.money -= 1
        return f'идёт в магазин, еда {House.food} штук; деньги осталось: {House.money} ден.ед.'

def day(person):
    number_cubes = randint(1, 6)
    if person.health < 0:
        print(f'К сожалению, {person.name} умер от голода.')
        return 1
    if person.health < 20 and House.food >= 10:
        text = person.eat()
    elif House.food < 10:
        text = person.shoping()
    elif House.money < 50:
        text = person.work()
    elif number_cubes == 1:
        text = person.work()
    elif number_cubes == 2:
        text = person.eat()
    else:
        text = person.play_games()
    print(person.name, text)
    return 0

person_1 = Person('Артём')
person_2 = Person('Сосед')

for i in range(1,366):
    print(f'========================= День {i} ===========================')
    if day(person_1) == 1 or day(person_2) == 1:
        print(f'Кто-то умер на {i} день')
    if i == 365:
        print('{blue}\nРебята прожили целый год вместе и выжили{endcolor}'.format(blue='\033[96m', endcolor='\033[0m'))
