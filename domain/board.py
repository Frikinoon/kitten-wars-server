from domain.board_exceptions import *


class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.kittens = set()

    def add_kitten(self, kitten):
        if kitten in self.kittens:
            raise KittenAlreadyPlayingException()
        elif not self._is_in_board(kitten):
            raise KittenInImpossibleLocationException()
        else:
            self.kittens.add(kitten)

    # TODO: Test json deserialization
    @staticmethod
    def from_json(dictionary):
        return Board(dictionary["height"], dictionary["width"])

    def _is_in_board(self, kitten):
        return kitten.x <= self.width and kitten.y <= self.height
