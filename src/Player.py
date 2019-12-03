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
        self.x_moves = [0, 1, 1, 1, 0, -1, -1, -1]
        self.y_moves = [1, 1, 0, -1, -1, -1, 0, 1]
        self.line_types = [0, 1, 2, 3, 4, 5, 6, 7]

    def get_move(self):
        import random
        opponent_moves = {}
        ai_moves = {}

        # determine and store where the opponent has their longest sequences
        for i in range(self.board.dimension):
            for j in range(self.board.dimension):
                if not self.board.is_empty(i, j):
                    for line in self.line_types:
                        opponent_position_and_length = self.board.sum_in_line(
                            self.name, i, j,
                            self.x_moves[line], self.y_moves[line], True)
                        opponent_moves[opponent_position_and_length] = line
                        ai_position_and_length = self.board.sum_in_line(
                            self.name, i, j,
                            self.x_moves[line], self.y_moves[line], False)
                        ai_moves[ai_position_and_length] = line

        # skim for the opponents longest sequences
        opponent_longest = 0
        for opponent_sequences in opponent_moves:
            if opponent_sequences[2] > opponent_longest:
                opponent_longest = opponent_sequences[2]
        ai_longest = 0
        for ai_sequences in ai_moves:
            if ai_sequences[2] > ai_longest:
                ai_longest = ai_sequences[2]

        # evaluate to win or block opponent
        while opponent_longest > 0:
            # block opponent
            for opp_line in opponent_moves:
                if opp_line[2] == opponent_longest:
                    if opponent_longest < 4:
                        segment = self.fill_fractured_sequence(opponent_moves)
                        if segment is not None:
                            return segment
                    if opponent_longest > 2:
                        if self.board.is_valid(opp_line[0], opp_line[1]):
                            if self.board.is_empty(opp_line[0], opp_line[1]):
                                return opp_line[0], opp_line[1]
            # attempt to win
            for ai_line in ai_moves:
                if ai_longest >= opponent_longest:
                    if ai_longest < 4:
                        segment = self.fill_fractured_sequence(ai_moves)
                        if segment is not None:
                            return segment
                    if ai_longest == 1:
                        if self.board.is_valid(ai_line[0], ai_line[1]):
                            if self.board.is_empty(ai_line[0], ai_line[1]):
                                if random.randint(1, 100) < 75:
                                    return ai_line[0], ai_line[1]
                    elif ai_longest == 2:
                        if self.board.is_valid(ai_line[0], ai_line[1]):
                            if self.board.is_empty(ai_line[0], ai_line[1]):
                                if random.randint(1, 100) < 85:
                                    return ai_line[0], ai_line[1]
                    elif ai_longest == 3:
                        if self.board.is_valid(ai_line[0], ai_line[1]):
                            if self.board.is_empty(ai_line[0], ai_line[1]):
                                if random.randint(1, 100) < 95:
                                    return ai_line[0], ai_line[1]
                    elif ai_longest == 4:
                        if self.board.is_valid(ai_line[0], ai_line[1]):
                            if self.board.is_empty(ai_line[0], ai_line[1]):
                                return ai_line[0], ai_line[1]

            opponent_longest -= 1

        # if no moves can be blocked or random move occurs, place a random piece
        while True:
            x = random.randint(0, self.board.dimension)
            y = random.randint(0, self.board.dimension)
            if self.board.is_empty(x, y):
                return x, y

    def fill_fractured_sequence(self, opponent_moves):
        # fill fractured segments
        for backend in opponent_moves:
            for frontend in opponent_moves:
                if opponent_moves[backend] == opponent_moves[frontend]:
                    if backend[2] == 2 and (
                            frontend[2] == 2 or frontend[2] == 1):
                        if frontend[0] - backend[0] == (frontend[2] + 1) * \
                                self.x_moves[opponent_moves[backend]]:
                            if frontend[1] - backend[1] == (frontend[2] + 1) * \
                                    self.y_moves[opponent_moves[backend]]:
                                if self.board.is_empty(backend[0], backend[1]):
                                    return backend[0], backend[1]
        return None


class HardAI(Player):

    def __init__(self, name: str, board: Board) -> None:
        Player.__init__(self, name, board)
        self.colour = (255, 65, 65)

    def get_move(self):
        temp = self.eval()
        return temp[0], temp[1]

    def eval(self) -> (int, int):
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
                                self._self_evaluation(self_eval, i, j, a, b)
                                # - end of self eval
                    else:
                        for a in range(-1, 2):
                            for b in range(-1, 2):
                                # - opp eval
                                self._opp_evaluation(opponent_eval, i, j, a, b)
                                # - end of opp eval
        # Handles 1st move by AI
        if number_of_pieces < 1:
            while True:
                x = random.randint(int(self.board.dimension / 2) - 1, int(self.board.dimension / 2) + 1)
                y = random.randint(int(self.board.dimension / 2) - 1, int(self.board.dimension / 2) + 1)
                move = (x, y)
                if self.board.is_empty(x, y):
                    return move

        else:
            # check for forced moves
            # find the max eval for both players in case there aren't any forced moves
            self_max = 0
            opponent_max = 0
            for x in self_eval:
                if self_eval[x] > self_max:
                    self_max = self_eval[x]
                if self_eval[x] > 4:
                    return x
            forced_blocks = {}
            for y in opponent_eval:
                if opponent_eval[y] > opponent_max:
                    opponent_max = opponent_eval[y]
                if opponent_eval[y] >= 3:
                    forced_blocks[y] = opponent_eval[y]
            if len(forced_blocks) > 0:
                for x in forced_blocks:
                    if forced_blocks[x] == opponent_max:
                        return x
            q = self_eval.copy()
            w = opponent_eval.copy()
            for x in q:
                if q[x] < self_max:
                    self_eval.pop(x)
            for y in w:
                if w[y] < opponent_max:
                    opponent_eval.pop(y)

        shared_moves = {}
        for x in self_eval:
            for y in opponent_eval:
                if x == y:
                    shared_moves[x] = self_eval[x], opponent_eval[x]
        if len(shared_moves) > 0:
            for x in shared_moves:
                temp = shared_moves[x]
                if temp[0] == self_max and temp[1] == opponent_max:
                    return x
        else:
            if self_max > opponent_max:
                # pick the attacking move that is closest to the centre
                move = -1, -1
                move_distance = 999
                for x in self_eval:
                    distance = (((x[0] + move[0])*(x[0] + move[0]) + (x[1] + move[1])*(x[1] + move[1]))*0.5)
                    if move_distance > distance:
                        move_distance = distance
                        move = x[0], x[1]
                return move
            else:
                for x in opponent_eval:
                    if opponent_eval[x] == opponent_max:
                        return x

    def _self_evaluation(self, self_eval,i,j,a,b):
        # - self eval
        temp = self.board.sum_in_line(self.name, i, j, a, b, False)
        if temp[0] != -1:
            if len(self_eval) > 0:
                exists = False
                for x in self_eval:
                    if x == (temp[0], temp[1]):
                        exists = True
                        break
                if exists:
                    current_val = self_eval[(temp[0]), (temp[1])]
                    new_val = (self.board.other_direction(self.name, i, j, 1 * a, 1 * b, False)) + temp[2]
                    if current_val < new_val:
                        self_eval[(temp[0]), (temp[1])] = new_val
                else:
                    self_eval[(temp[0]), (temp[1])] = temp[2]
                    self_eval[(temp[0]), (temp[1])] += self.board.other_direction(self.name, i, j, 1 * a, 1 * b, False)
            else:
                self_eval[(temp[0]), (temp[1])] = temp[2]
                self_eval[(temp[0]), (temp[1])] += self.board.other_direction(self.name, i, j, 1 * a, 1 * b, False)
        # - end of self eval

    def _opp_evaluation(self, opponent_eval, i, j, a, b):
        # - opp eval
        temp = self.board.sum_in_line(self.name, i, j, a, b, True)
        if temp[0] != -1:
            if len(opponent_eval) > 0:
                exists = False
                for x in opponent_eval:
                    if x == (temp[0], temp[1]):
                        exists = True
                        break
                if exists:
                    current_val = opponent_eval[(temp[0]), (temp[1])]
                    new_val = (self.board.other_direction(self.name, i, j, 1 * a, 1 * b, True)) + temp[2]
                    if current_val < new_val:
                        opponent_eval[(temp[0]), (temp[1])] = new_val
                else:
                    opponent_eval[(temp[0]), (temp[1])] = temp[2]
                    opponent_eval[(temp[0]), (temp[1])] += self.board.other_direction(self.name, i, j, 1 * a, 1 * b, True)
            else:
                opponent_eval[(temp[0]), (temp[1])] = temp[2]
                opponent_eval[(temp[0]), (temp[1])] += self.board.other_direction(self.name, i, j, 1 * a, 1 * b, True)
        # - end of opp eval
