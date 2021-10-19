violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

def list_of_song():
    song_list = []
    count_song = int(input('\nСколько песен Вы хотите выбрать? '))
    if count_song > len(violator_songs):
        print('Вы выбрали больше, чем девять любимых вами песен группы "Depeche Mode".', '\nПопробуйте ещё раз.')
        list_of_song()
    else:
        for i in range(count_song):
            print('Введите название', i+1, 'песни: ', end='')
            song_list.append(input())
        summ_timing = 0
        for timing in violator_songs:
            if timing[0] in song_list:
                summ_timing += timing[1]
        print('\nОбщее время звучания песен: ', float(round(summ_timing, 2)), 'минут')


list_of_song()