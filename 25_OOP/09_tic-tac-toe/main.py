class TicTacToeGame():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


    def __init__(self):
        pass

    def show_board(self):
        for cell_1, cell_2, cell_3 in self.board:
            print(f"\t {cell_1} | {cell_2} | {cell_3}")

    def set_cell_icon(self, icon, cell):
        row = int(cell / 3) - 1 if cell % 3 == 0 else int(cell / 3)
        col = 2 if cell == 3 else cell % 3 - 1
        self.board[row][col] = icon

    def get_game_status(self):
        counter = 0
        if (self.board[1][1] == self.board[0][0] and self.board[1][1] == self.board[2][2] or
            self.board[1][1] == self.board[0][2] and self.board[1][1] == self.board[2][0]) :
            self.current_player = self.player1 if self.board[1][1] == 'X' else self.player2
            return "Победил"
        for x in list(range(3)):
            if ( self.board[x][0] == self.board[x][1] and self.board[x][0] == self.board[x][2]):
                self.current_player = self.player1 if self.board[x][0] == 'X' else self.player2
                return "Победил"
            elif ( self.board[0][x] == self.board[1][x] and self.board[0][x] == self.board[2][x] ):
                self.current_player = self.player1 if self.board[0][x] == 'X' else self.player2
                return "Победил"
        for row in self.board:
            counter += row.count('X')
        if counter == 5:
            return "Ничья"
        else:
            return None

    def start_game(self):
        self.player1 = input("Введите имя первого игрока: ")
        self.player2 = input("Введите имя второго игрока: ")
        print(f"Игра в крестики нолики.\n {self.player1} против {self.player2}")
        self.player_icon = {self.player1: "X", self.player2: "0"}

        self.won_draw = None
        self.current_player = self.player1

        while self.won_draw == None:
            self.show_board()
            cell = int(input(f"{self.current_player} выберите где поставить ваш символ: "))
            self.set_cell_icon(self.player_icon.get(self.current_player), cell)
            self.current_player = self.player1 if self.current_player == self.player2 else self.player2

            self.won_draw = self.get_game_status()

    def show_results(self):
        self.show_board()
        if self.won_draw == 'Победил':
            print(f"{self.current_player} выиграл!")
        else:
            print(f"Хорошо сыграно! Ничья")

game_board = TicTacToeGame()
game_board.start_game()
game_board.show_results()