from Board import Board
import random


class Player:

    def __init__(self, name: str, board: Board):
        self.name = name
        self.board = board
        self.colour = (0, 0, 0)

    def make_a_move(self, x, y):
        """
        Makes a move on the board at position (x, y)
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

    def set_colour(self, colour):
        """
        Assigns a color to the player
        :param color
        """
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
        """
        Will return a weak move, in the form  (row, col)
        :return: (int row, int col)
        """
        move = self.board.all_around()
        if self.board.is_valid(move[0], move[1]) and move[0] != -1:
            return move[0], move[1]
        else:
            while True:
                x = random.randint(0, self.board.dimension)
                y = random.randint(0, self.board.dimension)
                if self.board.is_empty(x, y):
                    return x, y


class MediumAI(Player):
    """
    The MediumAI Class, responsible for returning moves to be played
    :param Player
    """

    def __init__(self, name: str, board: Board) -> None:
        Player.__init__(self, name, board)
        self.colour = (255, 65, 65)

    def get_move(self) -> (int, int):
        """
        Will return a strong move, in the form  (row, col)
        :return: (int row, int col)
        """
        # Calls the self.eval function and returns the given move
        temp = self.eval()
        return temp[0], temp[1]

    def eval(self) -> (int, int):
        """
        Will calculate strong moves that can be made by itself and the other player. The AI will determine the best
        move it should play, and will return that move
        :return: (int row, int col)
        """

        # Calculates a strong move to make, return the x,y position of that move
        number_of_pieces = 0
        # An evaluation dictionary of moves that the AI can make and that moves estimated strength
        self_eval = {}
        # An evaluation dictionary of moves that the Human Player can make and that moves estimated strength
        opponent_eval = {}
        for row in range(self.board.dimension):
            for col in range(self.board.dimension):
                if not self.board.is_empty(row, col):
                    if self.board.get_piece(row, col) == self.name:
                        number_of_pieces += 1
                        for d1 in range(-1, 2):
                            for d2 in range(-1, 2):
                                # Modifies the self_eval dictionary
                                self._self_evaluation(self_eval, row, col, d1, d2)

                    else:
                        for d1 in range(-1, 2):
                            for d2 in range(-1, 2):
                                # Modifies the opponent_eval dictionary
                                self._opp_evaluation(opponent_eval, row, col, d1, d2)

        # If the AI hasn't moved yet, it will make a move in the center of the board
        if number_of_pieces < 1:
            while True:
                x = random.randint(int(self.board.dimension / 2) - 1, int(self.board.dimension / 2) + 1)
                y = random.randint(int(self.board.dimension / 2) - 1, int(self.board.dimension / 2) + 1)
                move = (x, y)
                if self.board.is_empty(x, y):
                    return move

        else:
            # Will check for "forced moves" ie moves that mut be played
            # Will find the max strength evaluation (eval) for both players in case there aren't any forced moves

            # Stores the strength of the best move for future use
            self_max = 0
            opponent_max = 0
            for x in self_eval:
                if self_eval[x] > self_max:
                    self_max = self_eval[x]
                if self_eval[x] > 4:
                    return x
            # A dictionary with moves that must be made to stop the Human player from winning
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
        # A dictionary with useful moves that both players can make
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
                # Picks the attacking move that is closest to the centre
                move = -1, -1
                move_distance = 999
                for x in self_eval:
                    distance = (((x[0] + move[0]) * (x[0] + move[0]) + (x[1] + move[1]) * (x[1] + move[1])) * 0.5)
                    if move_distance > distance:
                        move_distance = distance
                        move = x[0], x[1]
                return move
            else:
                for x in opponent_eval:
                    if opponent_eval[x] == opponent_max:
                        return x

    def _self_evaluation(self, self_eval, row, col, d1, d2):
        """
        Modifies the self evaluation dictionary and finds strong moves that it  can make
        :param self_eval:
        :param row:
        :param col:
        :param d1:
        :param d2:
        :return: None
        """
        # A function that modifies the self evaluation dictionary
        temp = self.board.sum_in_line(self.name, row, col, d1, d2, False)
        if temp[0] != -1:
            if len(self_eval) > 0:
                exists = False
                for move in self_eval:
                    if move == (temp[0], temp[1]):
                        exists = True
                        break
                if exists:
                    current_val = self_eval[(temp[0]), (temp[1])]
                    new_val = (self.board.other_direction(self.name, row, col, 1 * d1, 1 * d2, False)) + temp[2]
                    if current_val < new_val:
                        self_eval[(temp[0]), (temp[1])] = new_val
                else:
                    self_eval[(temp[0]), (temp[1])] = temp[2]
                    self_eval[(temp[0]), (temp[1])] += self.board.other_direction(self.name, row, col, 1 * d1, 1 *
                                                                                  d2, False)
            else:
                self_eval[(temp[0]), (temp[1])] = temp[2]
                self_eval[(temp[0]), (temp[1])] += self.board.other_direction(self.name, row, col, 1 * d1, 1 *
                                                                              d2, False)

    def _opp_evaluation(self, opponent_eval, row, col, d1, d2):
        """
        Modifies the opponent dictionary and finds strong moves that the opponent can make
        :param opponent_eval:
        :param row:
        :param col:
        :param d1:
        :param d2:
        :return: None
        """
        # A function that modifies the opponent evaluation dictionary
        temp = self.board.sum_in_line(self.name, row, col, d1, d2, True)
        if temp[0] != -1:
            if len(opponent_eval) > 0:
                exists = False
                for move in opponent_eval:
                    if move == (temp[0], temp[1]):
                        exists = True
                        break
                if exists:
                    current_val = opponent_eval[(temp[0]), (temp[1])]
                    new_val = (self.board.other_direction(self.name, row, j, 1 * d1, 1 * d2, True)) + temp[2]
                    if current_val < new_val:
                        opponent_eval[(temp[0]), (temp[1])] = new_val
                else:
                    opponent_eval[(temp[0]), (temp[1])] = temp[2]
                    opponent_eval[(temp[0]), (temp[1])] += self.board.other_direction(self.name, row, j, 1 * d1, 1 * d2,
                                                                                      True)
            else:
                opponent_eval[(temp[0]), (temp[1])] = temp[2]
                opponent_eval[(temp[0]), (temp[1])] += self.board.other_direction(self.name, row, col, 1 * d1, 1 * d2,
                                                                                  True)


class HardAI(Player):
    def __init__(self, name: str, board: Board):
        Player.__init__(self, name, board)
        self.colour = (65, 65, 255)
        self.x_moves = [0, 1, 1, 1, 0, -1, -1, -1]
        self.y_moves = [1, 1, 0, -1, -1, -1, 0, 1]
        self.line_types = [0, 1, 2, 3, 4, 5, 6, 7]

    def get_move(self):
        """
        Will return best move, in the form  (row, col)
        :return: (int row, int col)
        """
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
