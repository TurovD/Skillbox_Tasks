import random

class Warrior:
  def __init__(self, health: int, name: str):
    self.health = health
    self.name = name

  def hit(self,target,target1):
    if target.health > 0:
      target.health -= 20
      print('\n',target1.name, 'атакует.')
      print(target.name,':',target.health, "HP")
    if target.health == 0:
      print(target1.name, "победил.")
      raise SystemExit

warrior1 = Warrior(100,"Первый Воин")
warrior2 = Warrior(100,"Второй Воин")


game = int(input("Введите 1 для атаки, 2 для прекращения работы программы: "))

while game != 2:
  if game == 1:
    probability = random.randint(1,11)
    if probability % 2 == 0:
      warrior1.hit(warrior2,warrior1)
      game = int(input("Введите 1 для атаки, 2 для прекращения работы программы: "))
    else:
      warrior2.hit(warrior1,warrior2)
      game = int(input("Введите 1 для атаки, 2 для прекращения работы программы: "))
  else:
    print("Wrong input.")
    break


