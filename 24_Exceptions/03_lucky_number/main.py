
import random

errors = [KeyboardInterrupt ,BaseException,ZeroDivisionError,SyntaxError,FileExistsError, AssertionError, AttributeError,ValueError,NameError,]
number_sum = 0
nums_file = open('nums.txt', 'w')
with nums_file as file:
    while number_sum <= 777:
        input_number = int(input('Введите число: '))
        number_sum += input_number
        if random.choices((0, 1), (1-1/13, 1/13))[0]:
            raise random.choice(errors)
        s=str(input_number)+'\n'
        nums_file.write(s)