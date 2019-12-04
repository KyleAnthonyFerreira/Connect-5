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
        """
        Will determine if any players have 5 pieces (or more) connected in a line
        :param player1:
        :param player2:
        :return: player1/2.name or ""
        """
        if self._connect_n(player1) >= 5:
            return player1.name
        elif self._connect_n(player2) >= 5:
            return player2.name
        else:
            return ""

    def _connect_n(self, player) -> int:
        """
        Will return the greatest number of pieces in a line for a specific player
        :param player:
        :return: int
        """
        max_value = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.get_piece(i, j) == player.name:
                    temp = self.connect_x(player, i, j)
                    if temp >= max_value:
                        max_value = temp
        return max_value

    def sum_in_line(self, player, row, col, d1, d2, is_player1) -> (int, int, int):
        """
        Used in some AI's, this function will determine how many pieces are connected in a line. This function will
        count for player 1 if is_player1 is true. Otherwise, this function will count for player2
        :param player:
        :param row:
        :param col:
        :param d1:
        :param d2:
        :param is_player1:
        :return:
        """
        # Used to scale the directions
        x = 0
        y = 0
        sum = 0

        if d1 == 0 and d2 == 0:
            return -1, -1, -1

        while True:
            if not is_player1:
                if self.is_valid(row + x, col + y):
                    if self.get_piece(row + x, col + y) == player:
                        sum += 1
                    elif self.is_empty(row + x, col + y):
                        return int(row + x), int(col + y), int(sum)
                    else:
                        break
                else:
                    return -1, -1, -1
                x = x + d1
                y = y + d2
            else:
                if self.is_valid(row + x, col + y):
                    if self.is_empty(row + x, col + y):
                        return int(row + x), int(col + y), int(sum)
                    elif self.get_piece(row + x, col + y) != player and not self.is_empty(row + x, col + y):
                        sum += 1
                    else:
                        break
                else:
                    return -1, -1, -1
                x = x + d1
                y = y + d2
        return -1, -1, -1

    def connect_x(self, player, row, col) -> int:
        """
        :param player:
        :param row:
        :param col:
        :return: bool
        """
        max_value = 0
        for d1 in range(-1, 2):
            # Used to scale the directions
            c = 1
            sum = 1
            d2 = -1
            while d2 < 2:
                if self.is_valid(row + (d1 * c), col + (d2 * c)):
                    if self.get_piece(row + (d1 * c),
                                      col + (d2 * c)) == player.name and not (
                            d1 == 0 and d2 == 0):
                        sum += 1
                    else:
                        c = 0
                        sum = 1
                        d2 += 1
                else:
                    c = 0
                    sum = 1
                    d2 += 1
                c += 1
                if sum >= max_value:
                    max_value = sum
        return max_value

    def other_direction(self, player, row, col, d1, d2, is_player1) -> int:
        """
        A function used by some AI's, used to calculate the number of pieces in a line at a given position in a given
        direction
        :param player:
        :param row:
        :param col:
        :param d1:
        :param d2:
        :param is_player1:
        :return: number of pieces that are in a line
        """
        if d1 == 0 and d2 == 0:
            return 0
        sum = 0
        c = 1
        while True:
            if self.is_valid(row+(d1*c), col+(d2*c)):
                if not is_player1:
                    if self.get_piece(row+(d1*c), col+(d2*c)) == player:
                        sum += 1
                    else:
                        return sum
                    c += 1
                else:
                    if self.get_piece(row+(d1*c), col+(d2*c)) != player and not self.is_empty(row+(d1*c), col+(d2*c)):
                        sum += 1
                    else:
                        return sum
                    c += 1
            return sum
