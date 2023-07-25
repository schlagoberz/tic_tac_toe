from exceptions import InvalidOperationException


class Board:
    def __init__(self):
        self.tiles = [[' ' for _ in range(3)] for _ in range(3)]
        self.next_player = "X"

    def make_move(self, row, column):
        self.make_move_internal(row, column, self.next_player)

    def make_move_internal(self, row, column, player):
        if row < 0 or row > 2:
            raise ValueError("Row index is out of range.")
        if column < 0 or column > 2:
            raise ValueError("Column index is out of range.")
        if player != self.next_player:
            raise ValueError("Only allowed symbols are: 'X' and 'O'.")
        if self.tiles[row][column] != " ":
            raise InvalidOperationException("Cannot make move since tile is already occupied.")

        self.tiles[row][column] = player
        self.next_player = "X" if player == "O" else "O"

    def is_game_over(self):
        return self.is_board_full() or self.has_winner()

    def is_board_full(self):
        for row in self.tiles:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def has_winner(self):
        winner = self.get_winner()
        return winner == "O" or winner == "X"

    def get_winner(self):
        winner = ""

        for row in range(len(self.tiles)):
            winner += self.get_winner_on_row(row)

        for column in range(len(self.tiles[0])):
            winner += self.get_winner_on_column(column)

        winner += self.get_winner_on_diagonals()

        return winner

    def get_winner_on_row(self, row):
        row_entries = self.tiles[row][0] + self.tiles[row][1] + self.tiles[row][2]
        return self.parse_winner_from_line(row_entries)

    def get_winner_on_column(self, column):
        column_entries = self.tiles[0][column] + self.tiles[1][column] + self.tiles[2][column]
        return self.parse_winner_from_line(column_entries)

    def get_winner_on_diagonals(self):
        main_diagonal = self.tiles[0][0] + self.tiles[1][1] + self.tiles[2][2]
        side_diagonal = self.tiles[2][0] + self.tiles[1][1] + self.tiles[0][2]

        return self.parse_winner_from_line(main_diagonal) + self.parse_winner_from_line(side_diagonal)

    def parse_winner_from_line(self, line):
        return "X" if line == "XXX" else "O" if line == "OOO" else ""
