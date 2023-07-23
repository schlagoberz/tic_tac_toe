from exceptions import InvalidOperationException


class Board:
    def __init__(self):
        self.tiles = [[' ' for _ in range(3)] for _ in range(3)]
        self.next_player = "X"

    def make_move(self, row, column):
        self._make_move(row, column, self.next_player)

    def _make_move(self, row, column, player):
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

    def can_make_move(self, row, column, player):
        return (0 <= row <= 2) and \
            (0 <= column <= 2) and \
            (player == self.next_player) and \
            (self.tiles[row][column] == " ")

    def is_game_over(self):
        return self.is_board_full() or self.has_winner()

    def is_board_full(self):
        for row in self.tiles:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def get_winner(self):
        # TODO: Implement me, plz.
        pass

    def has_winner(self):
        # TODO: Implement me, plz.
        pass
