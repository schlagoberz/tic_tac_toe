from exceptions import InvalidOperationException
from renderer import Renderer
from board import Board


class GameEngine:
    def __init__(self, board: Board, renderer: Renderer):
        self.board = board
        self.renderer = renderer

    def start(self):
        self.print_welcome_to_the_game()
        self.print_instructions()

        while not self.board.is_game_over():
            print(self.renderer.render_board())

            try:
                command = input(f"What's your next turn (1-9), player {self.board.next_player}?")
                move = self.parse_move_from_command(command)
                self.board.make_move(move[0], move[1])
            except KeyboardInterrupt:
                self.print_goodbye()
                return 0
            except InvalidOperationException as exception:
                print(str(exception))

        print(self.renderer.render_board())

        if self.board.has_winner():
            print(f"{self.board.get_winner()} has won the game!")
        else:
            print("Tie!")

    def print_welcome_to_the_game(self):
        message = "A console based Tic-Tac-Toe game."
        print(len(message) * "=")
        print(message)

    def print_instructions(self):
        message = """\
The game tiles are encoded by the numbers on 
the numpad in the following way:
"""
        print(len(message) * "=")
        print(message, end="")
        print("""\
[7][8][9]
[4][5][6]
[1][2][3]
""")
        print(len(message) * "=")

    def print_goodbye(self):
        print("\nSee you next time!")

    def parse_move_from_command(self, command):
        try:
            field_number = int(command)
            return self.parse_move_from_field_number(field_number)
        except ValueError:
            raise InvalidOperationException("Invalid player input. Please try again (1-9).")

    def parse_move_from_field_number(self, field_number):
        match field_number:
            case 1:
                return 2, 0
            case 2:
                return 2, 1
            case 3:
                return 2, 2
            case 4:
                return 1, 0
            case 5:
                return 1, 1
            case 6:
                return 1, 2
            case 7:
                return 0, 0
            case 8:
                return 0, 1
            case 9:
                return 0, 2
            case _:
                raise ValueError("Invalid field number provided.")
