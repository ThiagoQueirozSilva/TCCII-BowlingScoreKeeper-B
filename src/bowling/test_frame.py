from bowling.frame import Frame
import unittest


class TestFrames(unittest.TestCase):
    def test_Frame_Is_Strike(self):
        frame = Frame(10, 0)
        result = frame.is_strike()
        self.assertEqual(result, True)
    
    def test_Frame_Is_Strike_False(self):
        frame = Frame(6, 3)
        result = frame.is_strike()
        self.assertEqual(result, False)

    def test_Frame_Is_Strike_ButSpare(self):
        frame = Frame(6, 4)
        result = frame.is_strike()
        self.assertEqual(result, False)

    def test_Frame_Is_Spare(self):
        frame = Frame(5, 5)
        result = frame.is_spare()
        self.assertEqual(result, True)

    def test_Frame_Is_Spare_False(self):
        frame = Frame(2, 6)
        result = frame.is_spare()
        self.assertEqual(result, False)

    def test_Frame_Is_Spare_ButStrike(self):
        frame = Frame(10, 0)
        result = frame.is_spare()
        self.assertEqual(result, False)

    def test_Frame_Is_LastFrame(self):
        frame = Frame(10,0)
        result = frame.is_last_frame(10)
        self.assertEqual(result, True)
    
    def test_Frame_Bonus(self):
        frame = Frame(7,3)
        frame.bonus(4)
        self.assertEqual(frame.score, 14)

    def test_Frame_Score(self):
        frame = Frame(1,8)
        result = frame.score
        self.assertEqual(result, 9)
    
    def test_Frame_Score_With_Bonus(self):
        frame = Frame(10,0)
        frame.bonus(5)
        result = frame.score
        self.assertEqual(result, 15)
    
    def test_Frame_Validation(self):
        self.assertRaises(Exception("Não é possível derrubar mais de 10 pinos"), Frame(11,0))

if __name__ == '__main__':
    unittest.main()
