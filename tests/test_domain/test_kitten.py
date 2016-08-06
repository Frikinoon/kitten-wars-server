from nose.tools import eq_
from domain.kitten import Kitten


def test_kitten_instantiation():
    """Check if kitten instantiation assigns values correctly"""
    # Fixtures
    name = "Kitten Test"
    pos_x = 10
    pos_y = 12
    # Actual test
    kitten = Kitten(name, pos_x, pos_y)
    # Assertions
    eq_(kitten.name, name)
    eq_(kitten.x, pos_x)
    eq_(kitten.y, pos_y)