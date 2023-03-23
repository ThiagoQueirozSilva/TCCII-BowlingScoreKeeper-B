import unittest
from bowling.frame import Frame
from bowling.game import BowlingGame


class TestGames(unittest.TestCase):
    def test_Add_Frame(self):
        game = BowlingGame()
        frame = Frame(1, 2)
        game.add_frame(frame)
        numberOfFrames = game.frames.__len__
        self.assertEqual(2, numberOfFrames)

if __name__ == '__main__':
    unittest.main()
