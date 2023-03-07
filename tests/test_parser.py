import unittest

import parser


class TestGridSize(unittest.TestCase):
    def test_valid_grids(self):
        grids = {
            "0 0": (0, 0),
            "1 1": (1, 1),
            "99999      99999": (99999, 99999),
        }
        for k, v in grids.items():
            parsed = parser.parse_grid_size(k)
            self.assertEqual(parsed, v)

    def test_invalid_grids(self):
        grids = [
            "5, 5",
            "a 5",
            "5 a",
            "-1 5",
            "5 -1",
        ]
        for grid in grids:
            self.assertRaises(ValueError, lambda: parser.parse_grid_size(grid))


class TestParseRobot(unittest.TestCase):
    def test_valid_robots(self):
        robots = {
            "(0, 0, N)": ((0, 0), "N", ""),
            "(1, 0, E)": ((1, 0), "E", ""),
            "(0,0,S)F": ((0, 0), "S", "F"),
            "(99, 0, W)LRLRFF": ((99, 0), "W", "LRLRFF"),
        }

        for line, expected in robots.items():
            actual = parser.parse_robot(line)
            self.assertEqual(actual.pos, expected[0])
            self.assertEqual(actual.facing, expected[1])
            self.assertEqual(actual.commands, expected[2])

    def test_invalid_robots(self):
        robots = [
            "(0, 0, n)",
            "(0, 0, O)",
            "(O, 0, N)",
            "(0, 0, N",
            "0, 0, N)",
            "(0, 0, N)l",
            "(0, 0, N)r",
            "(0, 0, N)f",
            "(0, 0, N)A",
            "(0, -10, N)FFLR",
        ]

        for r in robots:
            self.assertRaises(ValueError, lambda: parser.parse_robot(r))


if __name__ == '__main__':
    unittest.main()
