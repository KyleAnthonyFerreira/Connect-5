from Player import Player


class Human(Player):

    def __init__(self, name: str):
        Player.__init__(self, name)

    def make_a_move(self):
        """
        Takes user input to make a move.
        :return: None
        """
        pass

