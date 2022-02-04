import random

random.seed()

class BlackJack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Королева', 'Король', 'Туз'] * 4
        self.score = 0
        self.bot_score = 0

    def card(self, current, score, bot):
        if not bot:
            print(f'Вам попалась карта {current}. У вас {score} очков.')
        else:
            print(f'Крупье попалась карта {current}. У крупье {score} очков')

    def random_card(self, score, bot):
        current = self.deck.pop()
        if type(current) is int:
            score += current
        elif current == 'Туз':
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += 10
        self.card(current, score, bot)
        return score

    def finish(self):
        while True:
            if input('\nХотите повторить? Да/нет \nВаш выбор: ').lower() == 'да':
                self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Королева', 'Король', 'Туз'] * 4
                self.start()
            else:
                print('До новых встреч!')
                break

    def choice(self):
        score = self.random_card(self.score, False)
        bot_score = self.random_card(self.bot_score, True)
        while True:
            print('----------------------------------')
            choice = input('Будете брать карту? да/нет\nВы выбираете: ')
            if choice.lower() == 'да':
                score = self.random_card(score, False)
                if bot_score < 19 and score <= 21:
                    bot_score = self.random_card(bot_score, True)
                if score > 21 or (bot_score == 21 and score != 21):
                    print('Извините, но вы проиграли')
                    break
                elif score == 21 and bot_score == 21:
                    print('Ничья')
                elif score == 21 or bot_score > 21:
                    print('Поздравляю, вы победили!')
                    break
            elif choice.lower() == 'нет':
                if score > bot_score and bot_score < 19:
                    while bot_score < 19:
                        bot_score = self.random_card(bot_score, True)
                if score < bot_score <= 21:
                    print(f'Вы проиграли, у вас {score} очков, у крупье {bot_score} очков')
                if score > bot_score:
                    print(f'Вы победили, у вас {score} очков, у крупье {bot_score} очков')
                if score == bot_score:
                    print('Ничья')

                break

    def start(self):
        random.shuffle(self.deck)
        print('\nВалеты, дамы и короли стоят по 10 очков.\nТуз может стоить 1 или 11 очков \n***************')
        self.choice()
        self.finish()

game = BlackJack()
game.start()