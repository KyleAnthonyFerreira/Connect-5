from src import Board
from src.Player import Player

"""
@AUTHOR: Joshua 
"""


class Human(Player):

    def __init__(self, name: str, board: Board):
        Player.__init__(self, name, board)

    def make_a_move(self, x, y):
        """
        Takes user input in the form (x,y) and attempts to make a move
        :param x: The Row of the board
        :param y: The Column of the board
        :return: None if the move was made, -1 if the move was not made due to the move being invalid
        """

        """
        1) Must check to see if the move given is valid...
            a) Is the x and y within the bounds of the board? (should always be true, since the user is using their 
            mouse to click on a tile)
            b) Is the tile at (x,y) empty?
        2) If 1) is true, then make the move, if 1) is false, return -1 to inform board that the move has not been made
            
        """
        # Checks to see if the (x, y) coordinate exists on the board
        if self.board.is_valid(x, y):
            # Checks to see if the tile at (x, y) is empty
            if self.board.is_empty(x, y):
                # If the above were true, then the move can be made
                # Note: The board has now been modified
                self.board.set_piece(self, x, y)
                return None

        # If any of the IF statements above failed, then the move was invalid
        # Note: The board was not modified
        return -1
