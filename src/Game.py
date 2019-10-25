from Player import Player
from Board import Board


class Game:
    def __init__(self, player1: Player, player2: Player, board: Board):
        """
        Initializes a game with a board and 2 players.
        :param player1:
        :param player2:
        :param board:
        """
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def is_winner(self, player: Player):
        """
        Determines if player won the game or not.
        :param player:
        :return: boolean
        """
        pass

    def is_game_over(self):
        """
        Determines whether or not the game is over.
        :return: boolean
        """
        pass

    def who_goes_next(self):
        """
        Determines who goes next.
        :return: self.player1 or self.player2
        """
        pass

    def make_move(self):
        """
        Makes a move on the board.
        (Will call is_game_over)
        :return: None
        """
        pass
