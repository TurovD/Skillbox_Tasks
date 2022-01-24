# TODO здесь писать код
user = input('Введите имя: ')

while True:
    print('\nЧтобы посмотреть текущий текст чата - введите <посмотреть> или <0>')
    print('Чтобы отправить сообщение - введите <отправить> или <1>')
    print('Чтобы выйти из чата - введите <выйти> или <2>')
    print('Чтобы выключить чат - введите <стоп> или <3>')
    action = input()

    if action == 'посмотреть' or action =='0':

        try:
            with open('chat.txt', 'r',encoding='utf-8') as file:
                for i_message in file:
                    print(i_message, end='')
        except FileNotFoundError:
            print('История сообщений пуста. \n')

    elif action == 'отправить' or action =='1':
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a',encoding='utf-8') as file:
            file.write(f' { user } : { message } \n')
    elif action == 'выйти' or action =='2':
        user = input('Введите имя: ')
    elif action == 'стоп' or action =='3':
        print("До встречи!")
        break
    else:
        print('Такой команды нет')
