import unittest
from ChessVar import *


class TestKingMove(unittest.TestCase):
    """

    """
    def test_1(self):
        """
        Tests out of bounds moves.
        """
        game = ChessVar()
        game.initialize_board()
        self.assertTrue(game.make_move('e1', 'e2'))
        game.initialize_board()
        self.assertTrue(game.make_move('e1', 'f1'))
        game.initialize_board()
        self.assertTrue(game.make_move('e1', 'd1'))
        game.initialize_board()
        self.assertFalse(game.make_move('e1', 'e0'))


    def test_2(self):
        """
        Tests piece specific movements.
        """

    def test_3(self):
        """
        Tests if a move is invalid due to an illegal jump.
        """