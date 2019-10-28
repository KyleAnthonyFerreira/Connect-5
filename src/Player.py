from src import Board


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


class EasyAI(Player):

    def __init__(self, name: str, board: Board):
        Player.__init__(self, name, board)

    def make_a_move(self, x, y):
        """
        Follows "Random" algorithm to make a move.
        :param x:
        :param y:
        :return: None
        """
        pass
