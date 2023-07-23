class GameEngine:
    def __init__(self, board, renderer):
        self.board = board
        self.renderer = renderer

    def start(self):
        while True:
            self.renderer.render()

            try:
                command = input("What's next?")
                match command:
                    case "w":
                        self.renderer.cursor_up()
                    case "s":
                        self.renderer.cursor_down()
                    case "a":
                        self.renderer.cursor_left()
                    case "d":
                        self.renderer.cursor_right()
                    case "e":
                        cursor = self.renderer.cursor
                        self.board.make_move(cursor[1], cursor[0])
                    case "q":
                        print("Bye!")
                        return 0
            except KeyboardInterrupt:
                return 0
