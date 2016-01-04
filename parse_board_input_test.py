import unittest
from parse_board_input import parse as parse_bi
from ship import Submarine, PatrolBoat, Aircraft


class TestParseBoardInput(unittest.TestCase):
    def test_input_1(self):
        expected = Submarine(('B', 2), True)
        input = "Place subMarine at B2 horizontally"
        self.assertEquals(parse_bi(input), expected)

    def test_input_2(self):
        expected = Aircraft(('E', 4), False)
        input = "place aircraft at E4 vertically"
        self.assertEquals(parse_bi(input), expected)

    def test_input_3(self):
        expected = PatrolBoat(('C', 6), False)
        input = "place patrol boat at C6 vertically"
        self.assertEquals(parse_bi(input), expected)

    def test_input_4(self):
        expected = PatrolBoat(('E', 3), True)
        input = "place patrol boats at E3 horizontally"
        self.assertEquals(parse_bi(input), expected)

    def test_invalid_ship(self):
        with self.assertRaises(ValueError):
            input = "Place sandwich on C3 horizontally"
            parse_bi(input)

    def test_invalid_position(self):
        with self.assertRaises(ValueError):
            input = "Place patrol boat on Z3 vertically"
            parse_bi(input)

    def test_invalid_orientation(self):
        with self.assertRaises(ValueError):
            input = "Place submarine on d1 diagonally"
            parse_bi(input)

if __name__ == '__main__':
    unittest.main()
