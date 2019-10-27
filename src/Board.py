from Player import Player #Neither of the import lines are working properly for some odd reason
from Game import Game

class Board:

    def __init__(self, dimension: int):
        """
        Initialize a dimension x dimension board.

        Note:
        "" indicates that the coordinate is empty
        "*" indicates that the coordinate is occupied by a piece from player1
        "." indicates that the coordinate is occupied by a piece from player2
        """
        self.dimension = dimension
        self.board = []

        # create the grid
        for y_coord in range(self.dimension):
            self.board.append([])
            for x_coord in range(self.dimension):
                self.board[y_coord].append([])

    def is_valid(self, x, y) -> Bool:
        """
        Return True iff the (x,y) coordinate is within the dimensions of the grid.

        :param x:
        :param y:
        :return:
        """

        if (x < 0) or (x > self.dimension - 1):
            return False
        if (y < 0) or (y > self.dimension - 1):
            return False

        return True

    def get_piece(self, x: int, y: int):
        """
        Returns player_name at coordinate(x, y)
        :param x:
        :param y:
        :return: String
        """

        for y_value in range(self.dimension):
            for x_coord in range(self.dimension):
                if self.board[y][x] == "":
                    return "That spot is empty."
                if self.board[y][x] == "*":
                    return "That spot is occupied by" + player1.name
                if self.board[y][x] == ".":
                    return "That spot is occupied by" + player2.name

    def set_piece(self, player: Player, x: int, y: int):
        """
        Places a piece for player at location (x,y)
        if possible.
        :param player:
        :param x:
        :param y:
        :return: None
        """

        for y_value in range(self.dimension):
            for x_value in range(self.dimension):
                if is_empty(x, y) == False:
                    return "Uh-oh. Move not applicable. Try another spot."
                if self.board[y][x] == "":
                    if player == self.player1:
                        self.board[y][x] = "*"
                    if player == self.player2:
                        self.board[y][x] = "."
        return str(player) + "has placed down their piece at coordinate (" + str(x) + "," + str(y) + ")!"

    def is_empty(self, x: int, y: int):
        """
        Return True iff coordinate (x,y) is unoccupied by a game piece.
        """

        if self.board[y][x] == "":
            return True

        return False


    def has_connect5(self, player: Player):
        """
        Return True iff there are 5 of the same game pieces in a row.

        Note: This can happen horizontally, vertically, and diagonally.

        :param player:
        :return: boolean
        """
        pass

