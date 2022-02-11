from random import randint, choice

names = ['Артем', 'Антон', 'Питер', 'Василий', 'Семен', 'Павел', 'Брюс','Роберт','Джон']
surnames = ['Уилис', 'Рэмбо', 'Паркер', 'Стоун', 'Паттисон','Орлов','Кузнецов','Сорокин','Вий']

def random_person():
    random_name = choice(names)
    random_surname = choice(surnames)
    random_age = randint(20, 70)
    return random_name, random_surname, random_age


class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'Мое имя: {self.__name} {self.__surname}. Мой возраст - {self.__age} .'


class Employee(Person):
    def calc_salary(self):
        raise Exception('Attention!')

    def __str__(self):
        return super().__str__() + f'\nМоя зарплата: {self.calc_salary()} рублей.\n'


class Manager(Employee):
    def calc_salary(self):
        return 13000


class Agent(Employee):
    sales: int

    def calc_salary(self):
        return 5000 + .05 * self.sales


class Worker(Employee):
    hours: int

    def calc_salary(self):
        return 100 * self.hours


if __name__ == '__main__':
    employees = list()

    for _ in range(3):
        employees.append(Manager(*random_person()))

    for _ in range(3):
        agent = Agent(*random_person())
        agent.sales = randint(2000, 10000)
        employees.append(agent)

    for _ in range(3):
        worker = Worker(*random_person())
        worker.hours = randint(20, 50)
        employees.append(worker)

    for employee in employees:
        print(employee)
