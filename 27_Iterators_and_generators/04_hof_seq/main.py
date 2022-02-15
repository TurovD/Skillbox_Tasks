class QHofstadter:
    def __init__(self, Q):
        self.Q = Q[:]

    def __next__(self):
        try:
            number = self.Q[-self.Q[-1]] + self.Q[-self.Q[-2]]
            self.Q.append(number)
            return number
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self

    def current_state(self):
        return self.Q

h = QHofstadter([1,1])
for i in range(1,int(input('Начиная с 3 числа, сколько чисел ряда вам нужно? '))+1):
    print(next(h))
