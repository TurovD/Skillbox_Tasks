class Student:

    def __init__(self, full_name, group_number, progress):
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress
        self.average = sum(progress) / len(progress)

    def give_average(self):
        return self.average

    def __str__(self):
        return f'{self.full_name} {self.group_number}'

    def good(self):
        good_progress = list(filter(lambda x: x in [4, 5], self.progress))
        return self.progress == good_progress


def receiving_data(i):
    name = input('\nФИ {} студента: '.format(i))
    group = input('Номер группы {} студента: : '.format(i))
    points = list(map(int, input('Успеваемость (оценки через пробел): ').split()))
    return name, group, points


list_student = [Student(*receiving_data(i)) for i in range(1,11)]
print('\nСписок студентов: ')
for student in list_student:
    print(student)

list_student.sort(key=lambda x: x.give_average())
print('\nОтсортированный список студентов: ')
for student in list_student:
    print(student)

print('\nСтуденты хорошисты и отличники:')
for student in list_student:
    if student.good():
        print(student)