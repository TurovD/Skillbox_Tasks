import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


file_1 = open('coordinates.txt', 'r')
file_2 = open('result.txt', 'w')

for line in file_1:
    nums_list = line.split()
    res1 = f(int(nums_list[0]), int(nums_list[1]))
    res2 = f2(int(nums_list[0]), int(nums_list[1]))
    number = random.randint(0, 100)
    my_list = sorted([res1, res2, number])
    file_2.write(' '.join(map(str,(my_list))) + '\n')

file_1.close()
file_2.close()
print("Сформирован список, состоящий из случайного числа и двух полученных результатов.")

