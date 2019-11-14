import random

class Player:

    #_colour: Tuple[int, int, int]
    name: str

    def __init__(self, colour, name: int) -> None:
        self._colour = colour
        self.name = name

    def set_colour(self, colour) -> None:
        self._colour = colour

    def get_move(self, dim) -> int:
        raise NotImplementedError



class AIEasy(Player):

    #_colour: Tuple[int, int, int]
    name: str

    def __init__(self, colour, name: int) -> None:
        Player.__init__(self, colour, name)

    def set_colour(self, colour) -> None:
        self._colour = colour

    def get_move(self, dim) -> int:
        while True:
            x = random.randint(0, dim)
            y = random.randint(0, dim)
            if Board.is_empty(x, y):
                return x, y

class AIMedium(Player):

    #_colour: Tuple[int, int, int]
    name: str

    def __init__(self, colour, name: str) -> None:
        Player.__init__(self, colour, name)
        
    def set_colour(self, colour) -> None:
        self._colour = colour

    def get_move(self) -> int:
        pass
        
