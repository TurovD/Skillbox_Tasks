class Property():
    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 500


print(' ***** Расчет налогов на имущество *****')
try:
    mount_money = float(input('Введите количество имеющихся денег: '))
    worth = float(input('Введите стоимость имущества: '))
    property_choose = int(input('Какой налог вам нужно рассчитать?\n'
                            '1 - Apartment\n'
                            '2 - Car\n'
                            '3 - CountryHouse\n'
                            '0 - Выход\n'
                            'Ваш выбор: '))
    if property_choose not in (1,2,3,0):
        raise ValueError
    if property_choose == 0:
        print("До свидания!")
except ValueError:
    print ("Ошибка! Неверный ввод. Попробуйте ещё раз.")
obj = Apartment(worth) if property_choose == 1 \
    else Car(worth) if property_choose == 2 \
    else CountryHouse(worth)
print ('\nНалог на имущество равен: ',obj.tax(),'\nДенег не хватает. Нужно ещё:', '-'
if mount_money - obj.tax() >= 0 else obj.tax() - mount_money)