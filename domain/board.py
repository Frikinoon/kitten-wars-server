class Board():
    def __init__(self, spec):
        self.height = spec.height
        self.width = spec.width
        self.kittens = set()

    def add_kitten(self, kitten):
        if kitten in self.kittens:
            raise KittenAlreadyPlayingException()
        elif not self._is_in_board(kitten):
            raise KittenInImpossibleLocationException()
        else:
            self.kittens.add(kitten)

    def _is_in_board(self, kitten):
        return kitten.x <= self.width and kitten.y <= self.height

class BoardSpec():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @staticmethod
    def from_json(dictionary):
        return Board(dictionary["height"], dictionary["width"])

class KittenAlreadyPlayingException(Exception):
    pass

class KittenInImpossibleLocationException(Exception):
    pass