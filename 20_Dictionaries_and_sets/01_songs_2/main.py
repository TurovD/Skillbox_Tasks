violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

number_song = int(input('Сколько песен выбрать? '))
time = round(sum([violator_songs[input(f'Название {i+1} песни: ')]
                 for i in range(number_song)]),2)
print('Общее время звучания песен: ',time,'минут.')