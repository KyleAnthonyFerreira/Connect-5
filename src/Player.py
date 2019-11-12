from src.Board import Board
import random


class Player:

    def __init__(self, name: str, board: Board):
        self.name = name
        self.board = board
        self.colour = (0, 0, 0)

    def make_a_move(self, x, y):
        """
        Implemented in children's class.
        :param x:
        :param y:
        :return: None
        """
        if self.board.is_valid(x, y):
            # Checks to see if the tile at (x, y) is empty
            if self.board.is_empty(x, y):
                # If the above were true, then the move can be made
                # Note: The board has now been modified
                self.board.set_piece(self, x, y)

    def get_move(self):
        pass


class Human(Player):

    def __init__(self, name: str, board: Board):
        Player.__init__(self, name, board)
        self.colour = (65, 255, 65)


class EasyAI(Player):

    def __init__(self, name: str, board: Board):
        Player.__init__(self, name, board)
        self.colour = (65, 65, 255)

    def get_move(self):
        while True:
            x = random.randint(0, self.board.dimension)
            y = random.randint(0, self.board.dimension)
            if self.board.is_empty(x, y):
                return x, y


class HardAI(Player):

    def __init__(self, name: str, board: Board) -> None:
        Player.__init__(self, name, board)
        self.colour = (255, 65, 65)

    def get_move(self) -> int:
        pass

    def eval(self) -> (int, int):
        self_eval = {}
        opponent_eval = {}

        for i in range(self.board.dimension):
            for j in range(self.board.dimension):
                if not self.board.is_empty(i, j):
                    for a in range(3):
                        for b in range(3):
                            c = 0
                            temp_eval = 0
                            stop = False
                            key = self.board.get_piece(i, j)
                            while not stop:
                                piece_at_tile = self.board.get_piece(i + (a - 1)*c, j + (b - 1)*c)

                                if not self.board.is_valid(i, j) or key != piece_at_tile:
                                    stop = True
                                elif self.board.is_empty(i + (a - 1) * c, j + (b - 1) * c):
                                    # Can make a move at (i+(a-1)*c, j+(b-1)*c)

                                    # Will check to see if the (i+(a-1)*c+1, j+(b-1)*c+1) tile is occupied by the AI
                                    # or the player, if it's occupied by the AI, then the eval will raise,
                                    # if it's occupied by the player, the eval becomes more tricky

                                    # Already will check if (i+(a-1)*c+1, j+(b-1)*c+1) is occupied by self, may add
                                    # more cases to increase IQ
                                    if key == "AI":
                                        self_eval[(i + (a - 1) * c, j + (b - 1) * c)] += temp_eval
                                    else:
                                        opponent_eval[(i + (a - 1) * c, j + (b - 1) * c)] += temp_eval
                                    stop = True
                                else:
                                    c += 1
                                    temp_eval += 1

        # Sort through the data and make a move
        self_score = -1
        self_position = (int(self.dimension - 1)/2, int(self.dimension - 1)/2)
        for position, value in self_eval.items():
            if value > self_score:
                self_score = value
                self_position = position
        opponent_score = -1
        opponent_position = (-1, -1)
        for position, value in opponent_eval.items():
            if value > self_score:
                opponent_score = value
                opponent_position = position

        # logic to return a good move
        if self_score >= 4:
            return self_position
        if opponent_score >= 4:
            return opponent_position
        if opponent_score > self_score:
            return opponent_position
        return self_position





