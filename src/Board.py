import random


class Board:

    def __init__(self, dimension: object) -> object:
        """
        Initialize a dimension x dimension board.
        """
        self.dimension = dimension
        self.board = []
        self.last_move = (0, 0)

        # create the grid
        for y_coord in range(self.dimension):
            self.board.append([])
            for x_coord in range(self.dimension):
                self.board[y_coord].append("")

    def is_valid(self, x, y) -> bool:
        """
        Return True iff the (x,y) coordinate is within the dimensions of the
        grid.
        :param x:
        :param y:
        :return: bool
        """

        if (x < 0) or (y > self.dimension - 1):
            return False
        if (y < 0) or (x > self.dimension - 1):
            return False

        return True

    def get_piece(self, x: int, y: int) -> str:
        """
        Returns player.name at coordinate(x, y) if the coordinate isn't empty.
        Else return "".
        :param x:
        :param y:
        :return: String
        """

        if self.is_empty(x, y):
            return ""
        else:
            return self.board[y][x]

    def set_piece(self, player, x: int, y: int) -> None:
        """
        Places a piece for player at location (x,y) if possible.
        :param player:
        :param x:
        :param y:
        :return: None
        """

        if self.is_empty(x, y):
            self.board[y][x] = player.name
            self.last_move = (x, y)

    def remove_piece(self, x: int, y: int) -> None:
        self.board[y][x] = ""

    def is_empty(self, x: int, y: int) -> bool:
        """
        Return True iff coordinate (x,y) is unoccupied by a game piece.
        :param x:
        :param y:
        :return: bool
        """

        if self.is_valid(x, y):
            if self.board[y][x] == "":
                return True

            return False

    def all_around(self):
        """
        Returns a random move around the last move made.
        :return: (int, int)
        """
        moves = []
        x = self.last_move[0]
        y = self.last_move[1]
        for x_direction in range(-1, 2):
            for y_direction in range(-1, 2):
                if self.is_valid(x + x_direction, y + y_direction):
                    if self.get_piece(x + x_direction, y + y_direction) == "":
                        moves.append((x + x_direction, y + y_direction))
        if len(moves):
            return random.choice(moves)
        else:
            return -1, -1

    def has_connect5(self, player1, player2):
        if self._connectN(player1) >= 5:
            return player1.name
        elif self._connectN(player2) >= 5:
            return player2.name
        else:
            return ""

    def _connectN(self, player) -> int:
        """
        :param player:
        :return: bool
        """
        max_value = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.get_piece(i, j) == player.name:
                    temp = self.connectX(player, i, j)
                    if temp >= max_value:
                        max_value = temp
        return max_value

    def sum_in_line(self, player, i, j, a, b) -> (int, int, int):
        x = 0
        y = 0
        sum = 0

        if a == 0 and b == 0:
            return -1, -1, -1

        while True:
            if self.is_valid(i + x, j + y):
                if self.get_piece(i + x, j + y) == player:
                    sum += 1
                elif self.is_empty(i + x, j + y):
                    return int(i + x), int(j + y), int(sum)
                else:
                    break
            else:
                return -1, -1, -1
            x = x + a
            y = y + b
        return -1, -1, -1

    def inverted_sum_in_line(self, player, i, j, a, b) -> (int, int, int):
        x = 0
        y = 0
        sum = 0

        if a == 0 and b == 0:
            return -1, -1, -1

        while True:
            if self.is_valid(i + x, j + y):
                if self.is_empty(i + x, j + y):
                    return int(i + x), int(j + y), int(sum)
                elif self.get_piece(i + x, j + y) != player and not self.is_empty(i + x, j + y):
                    sum += 1
                else:
                    break
            else:
                return -1, -1, -1
            x = x + a
            y = y + b
        return -1, -1, -1

    def connectX(self, player, i, j) -> int:
        """
                @TODO Make Look Nice :)
                :param player:
                :param i:
                :param j:
                :return: bool
                """
        max_value = 0
        for a in range(-1, 2):
            c = 1
            sum = 1
            b = -1
            while b < 2:
                if self.is_valid(i + (a * c), j + (b * c)):
                    if self.get_piece(i + (a * c),
                                      j + (b * c)) == player.name and not (
                            a == 0 and b == 0):
                        sum += 1
                    else:
                        c = 0
                        sum = 1
                        b += 1
                else:
                    c = 0
                    sum = 1
                    b += 1
                c += 1
                if sum >= max_value:
                    max_value = sum
        return max_value

    def inverted_connectX(self, player, i, j) -> int:
        """
                    @TODO Make Look Nice :)
                    :param player:
                    :param i:
                    :param j:
                    :return: bool
                    """
        max_value = 0
        for a in range(-1, 2):
            c = 1
            sum = 1
            b = -1
            while b < 2:
                if self.is_valid(i + (a * c), j + (b * c)):
                    if self.get_piece(i + (a * c),
                                      j + (b * c)) != player.name and not (
                            a == 0 and b == 0 and self.is_empty(i + (a * c),
                                                                j + (b * c))):
                        sum += 1
                    else:
                        c = 0
                        sum = 1
                        b += 1
                else:
                    c = 0
                    sum = 1
                    b += 1
                c += 1
                if sum >= max_value:
                    max_value = sum
        return max_value

    def other_direction(self, player, i, j, a, b) -> int:
        if a == 0 and b == 0:
            return 0
        sum = 0
        c = 1
        while True:
            if self.is_valid(i+(a*c), j+(b*c)):
                if self.get_piece(i+(a*c), j+(b*c)) == player:
                    sum += 1
                else:
                    return sum
                c += 1
            return sum

    def inverted_other_direction(self, player, i, j, a, b) -> int:
        if a == 0 and b == 0:
            return 0
        sum = 0
        c = 1
        while True:
            if self.is_valid(i+(a*c), j+(b*c)):
                if self.get_piece(i+(a*c), j+(b*c)) != player and not self.is_empty(i+(a*c), j+(b*c)):
                    sum += 1
                else:
                    return sum
                c += 1
            return sum

