ip_address = input('Введите IP: ').split('.')
if len(ip_address) != 4:
    print('Адрес - это четыре числа, разделенные точками')
else:
    for number in ip_address:
        if number.isdigit():
            control = True
            if int(number) > 255:
                control = False
                print(number,'превышает 255')
        else:
            control = False
            print(number, '- не целое число')
    if control is True:
        print('IP-адрес корректен')