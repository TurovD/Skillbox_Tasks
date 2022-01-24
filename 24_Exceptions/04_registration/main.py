def check_mail(string):
    name, email, age = string.split(' ')
    s = ('@', '.')
    age = int(age)
    if name.isalpha() is False:
        raise NameError
    elif age not in range(10,100):
        raise ValueError()
    else:
        for c in s:
            if c not in email:
                raise SyntaxError
    return string

with open('registrations.txt','r', encoding='utf-8') as registration_file:
    for string in registration_file:
        string = string[:-1]
        try:
            line = check_mail(string)
        except NameError:
            bad = open ('registration_bad.log', mode='a', encoding='utf-8')
            bad.write(string + ' - NameError' +'\n')
            bad.close()
        except SyntaxError:
            bad = open ('registration_bad.log', mode='a', encoding='utf-8')
            bad.write(string +' - SyntaxError' + '\n')
            bad.close()
        except ValueError:
            bad = open ('registration_bad.log', mode='a', encoding='utf-8')
            bad.write(string +' - ValueError'+ '\n')
            bad.close()
        else:
            good = open('registraton_good.log', mode='a', encoding='utf-8')
            good.write(string + '\n')
            good.close()

registration_file.close()
print("Данные из файла проверены,\nВ результате проверки сформируйте два файла:"
      "\nregistrations_good.log — для правильных данных,"
      "\nregistrations_bad.log — для ошибочных. ")