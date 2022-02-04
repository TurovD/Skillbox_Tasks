
class Circle:
    pi = 3.14159

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def get_area(self):
        area = self.r * self.r * self.pi
        print(area)

    def get_perimeter(self):
        return 2 * self.r * self.pi

    def scale(self, k):
        self.r *= k

    def is_intersect(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2

    def menu(self):
        choice = input('Что вы хотите сделать? \n1 - Найти Площадь \n2-  Найти Периметр \n3 - Увеличиваться круг в K раз \n4 - Определить, пересекается ли он с другой окружностью \nВам нужно: ')
        if choice == 1:
            self.get_area()
        if choice == 2:
           self.get_perimeter()
        if choice == 3:
            k = input('Во сколько раз вы хотите увеличить круг?')
            self.scale(k)
        if choice == 4:
            others = input('С каким кругом вы хотите найти пересечение? \nВведите номер круга: ')
            self.is_intersect(others)

circle = Circle()
circle.menu()