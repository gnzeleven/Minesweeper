from game import Game
from board import Board

# Initialize the board
boardSize = (9, 9)
prob = 0.20
board = Board(boardSize, prob)

# Create a game
screenSize = (800, 800)
game = Game(board, screenSize)

# Run the game
game.run()
