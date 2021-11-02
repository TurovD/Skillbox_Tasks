def input_password():
    password = list(input('\nПридумайте пароль: '))
    check_password(password)

def check_password(password):
    length_password =  len(password)
    upper_letter = sum(up_letter.isupper() for up_letter in password)
    count_numbers =  sum(number.isdigit() for number in password)
    if (length_password >= 8) and (upper_letter >= 1) and (count_numbers >= 3):
        print('Это надёжный пароль!')
    else:
        print ('Пароль ненадёжный. Попробуйте ещё раз.')
        input_password()



input_password()


