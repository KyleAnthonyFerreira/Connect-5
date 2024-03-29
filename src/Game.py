from Board import Board
from Player import Player


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
        self.next = player1
        self.board = board

    def whose_turn(self) -> Player:
        """
        Determines who the current turn belongs to.
        :return: self.player1 or self.player2
        """
        if self.next == self.player1:
            return self.player1
        else:
            return self.player2

    def who_goes_next(self) -> Player:
        """
        Determines who goes next.
        :return: self.player1 or self.player2
        """
        if self.next == self.player1:
            return self.player2
        else:
            return self.player1

    def is_winner(self) -> bool:
        """
        Determines if player won the game or not.
        :param player:
        :return: boolean
        """
        return self.board.has_connect5(self.player1, self.player2)

    def is_game_over(self) -> bool:
        """
        Determines whether or not the game is over.
        :return: boolean
        """
        if not self.is_winner() == "":
            return True
        else:
            for row in range(self.board.dimension):
                for column in range(self.board.dimension):
                    if self.board.is_empty(row, column):
                        return False
            return True

    def make_move(self, x: int, y: int) -> bool:
        """
         Makes a move on the board. Returns whether or not the move was
         successful.
        (Will call is_game_over)
        :param x:
        :param y:
        :return: boolean
        """
        if not self.is_game_over() and self.board.is_empty(x, y):
            self.next.make_a_move(x, y)
            self.next = self.who_goes_next()
            return True
        return False
