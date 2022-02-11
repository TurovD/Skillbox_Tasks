import math
class Automobile:
    def __init__(self, x, y, fi):
        self.x = x
        self.y = y
        self.fi = fi

    def move(self, dist):
        self.x = self.x + dist * math.cos(self.fi)
        self.y = self.y + dist * math.sin(self.fi)


class Bus(Automobile):
    money = 0
    passanger = 0
    def __init__(self,x,y,fi,money,passanger):
        super().__init__(x,y,fi)
        self.money = money
        self.passanger = passanger


    def move(self, dist):
        super().move(dist)
        self.money += self.passanger * dist

    def entrance(self, numbers_passanger):
        if int(numbers_passanger) > 0:
            self.passanger += numbers_passanger


    def exit(self, numbers_passanger_exit):
        if  int(numbers_passanger_exit) >= self.passanger:
            self.passanger = 0
        else:
            self.passanger -= numbers_passanger_exit

