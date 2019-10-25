class Game:

    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def is_winner(self, player):
        """
        Determines if player won the game or not.
        :param player:
        :return: true or false
        """
        pass

    def is_game_over(self):
        """
        Determines whether or not the game is over.
        :return: true or false
        """
        pass

    def who_goes_next(self):
        """
        Determines who goes next
        :return: self.player1 or self.player2
        """
        pass

    def make_move(self):
        """
        Makes a move on the board.
        (Will call is_winner and is_game_over)
        :return: None
        """
        pass
