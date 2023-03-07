import unittest

import robot


class TestTurn(unittest.TestCase):
    def test_turn_left(self):
        test_robot = robot.Robot('N', (0, 0), 'LLLL')
        test_robot.tick((10, 10))
        self.assertEqual(test_robot.facing, 'W')
        test_robot.tick((10, 10))
        self.assertEqual(test_robot.facing, 'S')
        test_robot.tick((10, 10))
        self.assertEqual(test_robot.facing, 'E')
        test_robot.tick((10, 10))
        self.assertEqual(test_robot.facing, 'N')

    def test_turn_right(self):
        test_robot = robot.Robot('N', (0, 0), 'RRRR')
        test_robot.tick((10, 10))
        self.assertEqual(test_robot.facing, 'E')
        test_robot.tick((10, 10))
        self.assertEqual(test_robot.facing, 'S')
        test_robot.tick((10, 10))
        self.assertEqual(test_robot.facing, 'W')
        test_robot.tick((10, 10))
        self.assertEqual(test_robot.facing, 'N')


class TestTick(unittest.TestCase):
    def test_drive_in_square(self):
        test_robot = robot.Robot('E', (0, 1), 'FRFRFRFR')
        c = 0
        while test_robot.is_active():
            test_robot.tick((2, 2))
            c += 1
        self.assertEqual(c, 8, "8 commands should have been executed")
        self.assertEqual(test_robot.pos, (0, 1), "Robot should be where it started")
        self.assertEqual(test_robot.facing, 'E', "Robot should be facing the same direction")

    def test_drive_off_left(self):
        test_robot = robot.Robot('W', (0, 0), 'F')
        test_robot.tick((10, 10))
        self.assertTrue(test_robot.lost)

    def test_drive_off_right(self):
        test_robot = robot.Robot('E', (9, 0), 'F')
        test_robot.tick((10, 10))
        self.assertTrue(test_robot.lost)

    def test_drive_off_top(self):
        test_robot = robot.Robot('N', (0, 9), 'F')
        test_robot.tick((10, 10))
        self.assertTrue(test_robot.lost)

    def test_drive_off_bot(self):
        test_robot = robot.Robot('S', (0, 0), 'F')
        test_robot.tick((10, 10))
        self.assertTrue(test_robot.lost)


if __name__ == '__main__':
    unittest.main()
