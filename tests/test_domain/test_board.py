from nose.tools import eq_, raises
from domain.kitten import Kitten
from domain.board import *


def test_board_instantiation():
    """Check Board instantiation assigns values correctly"""
    # Fixtures
    height = 10
    width = 20
    board_spec = BoardSpec(height, width)
    # Actual test
    board = Board(board_spec)
    # Assertions
    eq_(board.height, height)
    eq_(board.width, width)
    eq_(len(board.kittens), 0)


def test_add_non_existing_kitten():
    """Check adding a new kitten to the board works properly"""
    # Fixture
    board = Board(BoardSpec(height=20, width=20))
    new_kitten = Kitten("Kitten Test", 10, 10)
    # Actual test
    board.add_kitten(new_kitten)
    # Assertions
    eq_(board.kittens.__contains__(new_kitten), True)


@raises(KittenAlreadyPlayingException)
def test_add_existing_kitten_raise_exception():
    """Check adding existing kitten to the board raise KittenAlreadyPlayingException"""
    # Fixtures
    board = Board(BoardSpec(height=20, width=20))
    new_kitten = Kitten("Kitten test", 10, 10)
    board.add_kitten(new_kitten)
    # Actual test
    board.add_kitten(new_kitten)


@raises(KittenInImpossibleLocationException)
def test_adding_kitten_in_impossible_width():
    """Check adding kitten in impossible location width throws KittenInImpossibleLocationException"""
    # Fixture
    board = Board(BoardSpec(height=10, width=10))
    new_kitten = Kitten("kitten", 20, 10)
    # Actual test
    board.add_kitten(new_kitten)


@raises(KittenInImpossibleLocationException)
def test_adding_kitten_in_impossible_height():
    """Check adding kitten in impossible location height throws KittenInImpossibleLocationException"""
    # Fixture
    board = Board(BoardSpec(height=10, width=10))
    new_kitten = Kitten("kitten", 10, 20)
    # Actual test
    board.add_kitten(new_kitten)
