from Board import Board
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

    def set_colour(self, colour):
        self.colour = colour


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


class MediumAI(Player):

    def __init__(self, name: str, board: Board):
        Player.__init__(self, name, board)
        self.colour = (65, 65, 255)

    def get_move(self):
        move = self.board.all_around()
        if self.board.is_valid(move[0], move[1]) and move[0] != -1:
            return move[0], move[1]
        else:
            while True:
                x = random.randint(0, self.board.dimension)
                y = random.randint(0, self.board.dimension)
                if self.board.is_empty(x, y):
                    return x, y


class HardAI(Player):

    def __init__(self, name: str, board: Board) -> None:
        Player.__init__(self, name, board)
        self.colour = (255, 65, 65)

    def get_move(self):
        temp = self.eval()
        return temp[0], temp[1]

    def eval(self) -> (int, int):
        self_eval = {}
        opponent_eval = {}
        for i in range(self.board.dimension):
            for j in range(self.board.dimension):
                if self.board.is_empty(i, j):
                    self_eval[i, j] = self.board.connectX(self,i,j)
                    opponent_eval[i, j] = self.board.inverted_connectX(self,i,j)

        self_val = -1
        opp_val = -1

        for x in self_eval:
            if self_eval[x] >= self_val:
                self_val = self_eval[x]

        for y in opponent_eval:
            if opponent_eval[y] >= opp_val:
                opp_val = opponent_eval[y]

        if self_val >= 4:
            for x in self_eval:
                if self_eval[x] >= 4:
                    return x
        if opp_val >= 4:
            for y in opponent_eval:
                if opponent_eval[y] >=4:
                    return y
        if self_val >= opp_val:
            for x in self_eval:
                if self_eval[x] == self_val:
                    return x
        if opp_val > self_val and opp_val > 1:
            for y in opponent_eval:
                if opponent_eval[y] == opp_val:
                    return y
        while True:
            x = random.randint(0, self.board.dimension)
            y = random.randint(0, self.board.dimension)
            temp = (x,y)
            if self.board.is_empty(x, y):
                return temp





