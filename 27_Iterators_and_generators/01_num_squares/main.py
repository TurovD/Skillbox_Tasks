# класс-итератор
class Squared:
    def __init__(self,N):
        self.__N = N
        self.__counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if int(self.__counter) <= int(self.__N):
            number = int(self.__counter)**2
            self.__counter += 1
            return number
        else:
           raise StopIteration

N = int(input('Введите число N: '))
print('Класс-итератор')
class_iter = Squared(N)
for num in class_iter:
    print(num)

# функция-генератор
def gen_squad(Num):
    for _ in range(1,Num+1):
        cur_val = _ ** 2
        yield cur_val
        if cur_val > N**2:
            return
print('\nФункция-генератор')
gen_squad = gen_squad(N)
for i_value in gen_squad:
    print(i_value, end = ' ')
print()


# генераторное выражение
print('\nГенераторное выражение')
squared_gen = (number ** 2 for number in range(1,N+1))
for i_num in squared_gen:
    print(i_num, end=' ')