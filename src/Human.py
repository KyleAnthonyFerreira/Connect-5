from Player import Player


class Human(Player):

    def __init__(self, name: str, board: Board):
        Player.__init__(self, name, board)

    def make_a_move(self, x, y):
        """
        Takes user input to make a move.
        :param x:
        :param y:
        :return: None
        """
        pass
