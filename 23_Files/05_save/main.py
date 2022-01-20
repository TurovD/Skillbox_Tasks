
import os
def reads(path):
    file = open(path, 'r')
    print("\nСодержимое файла: \n", file.read())
    file.close()

def saves(string):
    way = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ')
    file_name = input('Введите имя файла: ')
    r_path = way.replace(" ", "/")
    real_path = os.path.join(r_path, file_name)
    path = str('C:/' + real_path)
    check_file = os.path.exists(path)
    if check_file:
        print('Файл с таким именем уже существует!')
        ans_q = input('Вы действительно хотите перезаписать файл? ').lower()
        if ans_q == 'да' or ans_q == 'yes':
            f = open(path, 'w')
            f.write(string)
            f.close()
            print('Файл успешно перезаписан!')
            reads(path)
        else:
            print('Файл не перезаписан')
    else:
        f = open(path, 'w')
        f.write(string)
        f.close()
        print('Файл успешно сохранён!')
        reads(path)


saves(str(input('Введите строку: ')))
