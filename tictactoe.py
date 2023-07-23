from board import Board
from game_engine import GameEngine
from renderer import Renderer

if __name__ == "__main__":
    board = Board()
    renderer = Renderer(board)
    game_engine = GameEngine(board, renderer)
    game_engine.start()
