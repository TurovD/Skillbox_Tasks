class Parents:
    def __init__(self, name, age, childs):
        self.name = name
        self.age = age
        self.childs = childs

    def __str__ (self):
        return self.name + ' возраст: ' + str(self.age) +' лет \nДети: \n' + '\n'.join([str(child) for child in self.childs])

    def calm(self, child):
        for children in self.childs:
            if children is child:
                children.is_Serenity = True

    def feed(selfs, child):
        for children in selfs.childs:
            if children is child:
                children.is_Hungry = True

class Child:
    def __init__(self, name, age, is_Serenity, is_Hungry):
        self.name = name
        self.age = age
        self.is_Serenity = is_Serenity
        self.is_Hungry = is_Hungry

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' лет. Ребёнок ' +  (' cпокоен. '
        if self.is_Serenity else 'раздражен.') + (' Ребенок сыт' if self.is_Hungry else 'Ребенок хочет кушать')

Anzelika = Child('Анжелика', 15, False,True)
Nina = Child('Нина', 5, True,True)
grisha = Parents('Григорий',42,[Anzelika,Nina])
print(grisha)
if input('Успокоить Анжелику? Да/Нет \nВаш выбор: ').lower() =='да':
    grisha.calm(Anzelika)
    print(grisha)
else:'Очень жаль.'