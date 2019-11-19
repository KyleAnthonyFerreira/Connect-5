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
        # print(self.name) == Player 2
        number_of_pieces = 0
        self_eval = {}
        opponent_eval = {}
        for i in range(self.board.dimension):
            for j in range(self.board.dimension):
                if not self.board.is_empty(i, j):
                    if self.board.get_piece(i, j) == self.name:
                        number_of_pieces += 1
                        for a in range(-1, 2):
                            for b in range(-1, 2):
                                # - self eval
                                temp = self.board.sum_in_line(self.name, i, j, a, b)
                                if temp[0] != -1:
                                    if len(self_eval) > 0:
                                        exists = False
                                        for x in self_eval:
                                            if x == (temp[0], temp[1]):
                                                exists = True
                                                break
                                        if exists:
                                            self_eval[(temp[0]), (temp[1])] += temp[2]

                                        else:
                                            self_eval[(temp[0]), (temp[1])] = temp[2]
                                    else:
                                        self_eval[(temp[0]), (temp[1])] = temp[2]
                                # - end of self eval

                                # - opp eval
                                temp = self.board.inverted_sum_in_line(self.name, i, j, a, b)
                                if temp[0] != -1:
                                    if len(opponent_eval) > 0:
                                        exists = False
                                        for x in opponent_eval:
                                            if x == (temp[0], temp[1]):
                                                exists = True
                                                break
                                        if exists:
                                            opponent_eval[(temp[0]), (temp[1])] += temp[2]
                                        else:
                                            opponent_eval[(temp[0]), (temp[1])] = temp[2]
                                    else:
                                        opponent_eval[(temp[0]), (temp[1])] = temp[2]
                                # - end of opp eval
        # Handles 1st move by AI
        if number_of_pieces < 1:
            while True:
                x = random.randint(int(self.board.dimension / 2) - 1, int(self.board.dimension / 2) + 1)
                y = random.randint(int(self.board.dimension / 2) - 1, int(self.board.dimension / 2) + 1)
                temp = (x, y)
                if self.board.is_empty(x, y):
                    print("MOVE")
                    print(temp)
                    return temp
        else:
            max = 0
            temp_move = -1, -1
            for x in self_eval:
                if self_eval[x] >= max:
                    max = self_eval[x]
                    temp_move = x

            if max >= 4:
                return temp_move
            else:
                max_op = 0
                temp_move_op = -1, -1
                for x in opponent_eval:
                    if opponent_eval[x] >= max_op:
                        max_op = opponent_eval[x]
                        temp_move_op = x

            if max >= max_op:
                return temp_move
            else:
                return temp_move_op

            return temp_move



