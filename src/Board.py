from Player import Player

DIM = 19


class Board:

    def __init__(self, dimension=DIM):
        """
        Initialize a DIMxDIM board.
        """
        self.dimension = dimension
        # make the grid

    def get_piece(self, x: int, y: int):
        pass

    def set_piece(self, player: Player, x: int, y: int):
        """
        Places a piece for player at location (x,y)
        if possible.
        :param player:
        :param x:
        :param y:
        :return: None
        """
        pass

    def is_empty(self, x: int, y: int):
        """
        Checks if space at (x,y) is empty.
        :param x:
        :param y:
        :return: boolean
        """
        pass

    def has_connect5(self, player: Player):
        """
        Checks if player has 5 pieces in a row.
        :param player:
        :return: boolean
        """
        pass

