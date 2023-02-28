class TicTacToe:
    def __init__(self, rows, cols, winning=None):
        self.rows = rows
        self.cols = cols
        if winning is not None and (winning > rows or winning > cols):
            raise ValueError("Winning length cannot be greater than the board size")
        self.winning = winning
        self.board = [['-' for j in range(self.cols)] for i in range(self.rows)]
        self.occupied = dict()
        
    def show_current_board(self):
        for idx, tiles in enumerate(self.board):
          tiles_str = f'{tiles}' + '\n' if idx == len(self.board) - 1 else f'{tiles}'
          print(tiles_str)
        return
    
    def update_board(self, mark, row, col):
        self.board[row][col] = mark

    def check_win(self, mark):
        # Check horizontal rows
        for row in self.board:
            if self.winning is not None and self.winning >= 0:
                if self._consecutive_count(row, mark) >= self.winning:
                    return True
            if row.count(mark) == len(row):
                return True

        # Check vertical columns
        for col in range(len(self.board[0])):
            if self.winning:
                columns = [self.board[row][col] for row in range(len(self.board))]
                if self._consecutive_count(columns, mark) >= self.winning:
                    return True
            if all(self.board[row][col] == mark for row in range(len(self.board))):
                return True

        # Check diagonal lines
        if all(diag == mark for diag in self.get_diagonal()) or all(diag == mark for diag in self.get_diagonal(True)):
            return True
        if self.winning:
            if self._consecutive_count(self.get_diagonal(), mark) >= self.winning or self._consecutive_count(self.get_diagonal(True), mark) >= self.winning:
                return True
            
        # No winning combination found
        return False

    
    def get_diagonal(self, flipped=False):
        if not flipped:
            return [self.board[i][i] for i in range(len(self.board))]
        return [self.board[i][len(self.board)-i-1] for i in range(len(self.board))]
    
    def get_user_input(self):
        while True:
            row = int(input(f"Enter row number (0-{self.rows-1}): "))
            col = int(input(f"Enter column number (0-{self.cols-1}): "))
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                print("Invalid input. Please try again.")
            elif self.occupied.get((row, col)):
                print("You cannot mark an already selected box")
                self.show_current_board()
            else:
                return row, col


    def play_game(self):
        self.show_current_board()
        player = 'X'
        while True:
            print(f"Player {player}'s turn")
            row, col = self.get_user_input()
            self.update_board(player, row, col)
            self.occupied[(row, col)] = player
            self.show_current_board()
            if self.check_win(player):
                print(f"Player {player} wins!")
                break
            if "-" not in [square for row in self.board for square in row]:
                print("Game over. It's a tie!")
                break
            # switch player turn
            player = 'O' if player == 'X' else 'X'
    
    @staticmethod
    def _consecutive_count(lst, mark):
        """
        Returns the maximum number of consecutive occurrences of `mark` in `lst`.
        """
        max_count = 0
        count = 0
        for item in lst:
            if item == mark:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)


if __name__ == '__main__':
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    winning = input("Enter lenght of winning row or column: (optional)")
    winning = int(winning) if winning else None
    board = TicTacToe(rows, cols, winning)
    board.play_game()   