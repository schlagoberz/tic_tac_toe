class Renderer:
    def __init__(self, board):
        self.board = board
        self.cursor = [0, 0]

    def cursor_up(self):
        self.move_cursor(0, -1)

    def cursor_down(self):
        self.move_cursor(0, 1)

    def cursor_right(self):
        self.move_cursor(1, 0)

    def cursor_left(self):
        self.move_cursor(-1, 0)

    def move_cursor(self, delta_x, delta_y):
        new_x = self.cursor[0] + delta_x
        new_y = self.cursor[1] + delta_y

        self.cursor[0] = new_x if 0 <= new_x <= 2 else self.cursor[0]
        self.cursor[1] = new_y if 0 <= new_y <= 2 else self.cursor[1]

    def render_row(self, row_index):
        print(9 * "#")
        for column_index in range(len(self.board.tiles[row_index])):
            self.render_cell(row_index, column_index)
        print("\n", end="")
        print(9 * "#")

    def render_cell(self, row_index, column_index):
        print("#", self.symbol_at(row_index, column_index), "#", sep="", end="")

    def symbol_at(self, row_index, column_index):
        symbol = self.board.tiles[row_index][column_index]
        return symbol if not self.is_cursor_at(row_index, column_index) else "^"

    def is_cursor_at(self, row_index, column_index):
        return self.cursor == [column_index, row_index]

    def render(self):
        for row_index in range(len(self.board.tiles)):
            self.render_row(row_index)
