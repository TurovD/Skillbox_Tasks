special_symbol, work_cycle = list('@№$%^&*()'), True

while work_cycle is not False:
    checking_input = True
    file_name = input('\nВведите название файла: ')
    if not file_name.endswith(('.txt', '.docx')):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
        checking_input = False
    for i in range(len(special_symbol)):
        if file_name.startswith(special_symbol[i]):
            print('Ошибка: название начинается на один из специальных символов')
            checking_input = False
    if  checking_input is not False:
        print('Файл назван верно.')
        break