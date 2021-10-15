films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
def favourits_movie():
    for i in range(1, numbers_movie + 1):
        print('Введите название', i, 'фильма (с заглавной буквы): ', end='')
        movie_names = input()
        if movie_names not in films:
            print('К сожалению, такого фильма у нас нет, но мы скоро его добавим.')
            choice = input('Вы хотите ознакомиться с фильмами, которые у нас есть? ')
            if choice == 'да' or choice == 'Да':
                print(films,'\nЕсли хотите добавить фильм из списка, введите его название (с заглавной буквы), если нет и закончить, то введите 0: ',end='')
                movie_names = input()
                if movie_names == '0':
                    break
                else:
                    favourite_movie.append(movie_names)
            else:
                finish=input('Вы хотите закончить? ')
                if finish == 'да' or 'Да':
                    print('До свидания.',end=' ')
                    break
        else:
            favourite_movie.append(movie_names)

favourite_movie = []
numbers_movie = int(input('Сколько фильмов вы хотите добавить? '))
favourits_movie()
print('Список любимых фильмов: ',*favourite_movie, end=' ')