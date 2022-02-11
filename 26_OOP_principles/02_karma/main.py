import random

class Life:
    __target_karma = 500
    __karma = 0

    def get_target_karma(self):
        return self.__target_karma

    def get_karma(self):
        return self.__karma

    def set_karma(self,point):
        self.__karma += point

    def reach_enlightment(self):
        if self.get_karma() >= self.get_target_karma():
            return True

    def one_day(life):
        sin_num = random.randint(1, 10)
        attention = ['KillError','DrunkError','CarCrashError','GluttonyError','DepressionError']

        try:
            if sin_num == 10:
                raise BaseException
        except BaseException:
            exception = random.choice(attention)
            return exception
        else:
            life.set_karma(random.randint(1, 7))

human_life = Life()
days_passed = 0
karma_log = []

while True:
    if human_life.reach_enlightment():
        print('Просветление произошло через {} дней'.format(days_passed))
        break
    else:
        day = human_life.one_day()
        days_passed += 1
        if day is not None:
            with open('karma.log','a') as file:
                file.write(day)
                file.write(' ')
            karma_log.append(day)

print(karma_log)