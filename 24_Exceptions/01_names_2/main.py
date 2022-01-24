line_count = 0
sym_sum = 0
people_file = open('people.txt','r')
errors_file = open("errors.log.txt", "w")
while True:
    try:
        for i_line in people_file:
            line_count +=1
            length = len(i_line)
            if i_line.endswith("\n"):
                length -= 1
            if length < 3:
                raise BaseException
            sym_sum +=length
        print('Количество символов равно: ',sym_sum)
        people_file.close()
        errors_file.close()
        break
    except BaseException:
        print('Длина {} строки меньше 3 символов'.format(line_count))
        errors_file.write('\nПроблема заключается в {} строке'.format(line_count))

