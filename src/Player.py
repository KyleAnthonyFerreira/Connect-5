from Board import Board


class Player:

    def __init__(self, name: str, board: Board):
        self.name = name
        self.board = board

    def make_a_move(self, x, y):
        """
        Implemented in children's class.
        :param x:
        :param y:
        :return: None
        """
        pass

