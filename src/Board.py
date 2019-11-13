class Board:

    def __init__(self, dimension: object) -> object:
        """
        Initialize a dimension x dimension board.
        """
        self.dimension = dimension
        self.board = []

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

    def has_connect5(self, player) -> bool:
        """
        Return True iff there are exactly 5 of the same game pieces in a linear
        line.
        Note: This can happen horizontally, vertically, and diagonally.
        :param: player
        :return: boolean
        """

        line_counter = 0

        for y_coord in range(len(self.board)):
            for x_coord in range(len(self.board[y_coord])):
                if self.board[y_coord][x_coord] == player.name:
                    line_counter += 1

                    # checks if there is connect5 horizontally
                    if self.board[y_coord][x_coord + 1] == player.name:
                        line_counter += 1
                        if self.board[y_coord][x_coord + 2] == player.name:
                            line_counter += 1
                            if self.board[y_coord][x_coord + 3] == player.name:
                                line_counter += 1
                                if self.board[y_coord][
                                        x_coord + 4] == player.name:
                                    line_counter += 1
                    if line_counter == 5:
                        return True
                    else:
                        line_counter = 1

                    # checks if there is connect5 vertically
                    if self.board[y_coord + 1][x_coord] == player.name:
                        line_counter += 1
                        if self.board[y_coord + 2][x_coord] == player.name:
                            line_counter += 1
                            if self.board[y_coord + 3][x_coord] == player.name:
                                line_counter += 1
                                if self.board[y_coord + 4][
                                        x_coord] == player.name:
                                    line_counter += 1
                    if line_counter == 5:
                        return True
                    else:
                        line_counter = 1

                    # checks if there is connect5 diagonally upwards
                    if self.board[y_coord + 1][x_coord - 1] == player.name:
                        line_counter += 1
                        if self.board[y_coord + 2][x_coord - 2] == player.name:
                            line_counter += 1
                            if self.board[y_coord + 3][
                                    x_coord - 3] == player.name:
                                line_counter += 1
                                if self.board[y_coord + 4][
                                        x_coord - 4] == player.name:
                                    line_counter += 1
                    if line_counter == 5:
                        return True
                    else:
                        line_counter = 1

                    # checks if there is connect5 diagonally downwards
                    if self.board[y_coord + 1][x_coord + 1] == player.name:
                        line_counter += 1
                        if self.board[y_coord + 2][x_coord + 2] == player.name:
                            line_counter += 1
                            if self.board[y_coord + 3][
                                    x_coord + 3] == player.name:
                                line_counter += 1
                                if self.board[y_coord + 4][
                                        x_coord + 4] == player.name:
                                    line_counter += 1
                    if line_counter == 5:
                        return True
                    else:
                        line_counter = 1

        return False

    def has_connect4(self, player) -> bool:
        """
        Return True iff there are exactly 4 of the same pieces in a linear line.
        Note: This can happen horizontally, vertically, and diagonally.
        :param: player
        :return: boolean
        """
        # We may need this function for the intermediate level AI

        line_counter = 0

        for y_coord in range(len(self.board)):
            for x_coord in range(len(self.board[y_coord])):
                if self.board[y_coord][x_coord] == player.name:
                    line_counter += 1

                    # checks if there is connect5 horizontally
                    if self.board[y_coord][x_coord + 1] == player.name:
                        line_counter += 1
                        if self.board[y_coord][x_coord + 2] == player.name:
                            line_counter += 1
                            if self.board[y_coord][x_coord + 3] == player.name:
                                line_counter += 1
                    if line_counter == 4:
                        return True
                    else:
                        line_counter = 1

                    # checks if there is connect5 vertically
                    if self.board[y_coord + 1][x_coord] == player.name:
                        line_counter += 1
                        if self.board[y_coord + 2][x_coord] == player.name:
                            line_counter += 1
                            if self.board[y_coord + 3][x_coord] == player.name:
                                line_counter += 1
                    if line_counter == 4:
                        return True
                    else:
                        line_counter = 1

                    # checks if there is connect5 diagonally upwards
                    if self.board[y_coord + 1][x_coord - 1] == player.name:
                        line_counter += 1
                        if self.board[y_coord + 2][x_coord - 2] == player.name:
                            line_counter += 1
                            if self.board[y_coord + 3][
                                    x_coord - 3] == player.name:
                                line_counter += 1
                    if line_counter == 4:
                        return True
                    else:
                        line_counter = 1

                    # checks if there is connect5 diagonally downwards
                    if self.board[y_coord + 1][x_coord + 1] == player.name:
                        line_counter += 1
                        if self.board[y_coord + 2][x_coord + 2] == player.name:
                            line_counter += 1
                            if self.board[y_coord + 3][
                                    x_coord + 3] == player.name:
                                line_counter += 1
                    if line_counter == 4:
                        return True
                    else:
                        line_counter = 1

        return False
