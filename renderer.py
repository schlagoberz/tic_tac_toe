class Renderer:
    def __init__(self, board):
        self.board = board

    def render_board(self):
        board = ""
        for row_index in range(len(self.board.tiles)):
            board += self.render_row(row_index) + "\n"
        return board

    def render_row(self, row_index):
        row = ""
        for column_index in range(len(self.board.tiles[row_index])):
            row += self.render_cell(row_index, column_index)
        return row

    def render_cell(self, row_index, column_index):
        return f"[{self.board.tiles[row_index][column_index]}]"
