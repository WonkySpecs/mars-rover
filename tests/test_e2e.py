"""End to end tests on example inputs"""
import os
import unittest

import main
import parser

_examples_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'examples')


class TestE2E(unittest.TestCase):
    def test_run_example_1(self):
        fname = os.path.join(_examples_dir, 'example-1')
        with open(fname) as f:
            grid_size, robots = parser.parse_lines(f.readlines())

        final = main.run(grid_size, robots)

        self.assertEqual(2, len(final), "2 robots should have run")
        self.assertEqual(final[0], '(3, 4, E) LOST')
        self.assertEqual(final[1], '(0, 4, W) LOST')

    def test_run_example_2(self):
        fname = os.path.join(_examples_dir, 'example-2')
        with open(fname) as f:
            grid_size, robots = parser.parse_lines(f.readlines())

        final = main.run(grid_size, robots)

        self.assertEqual(2, len(final), "2 robots should have run")
        self.assertEqual(final[0], '(2, 3, W)')
        self.assertEqual(final[1], '(1, 0, S) LOST')


if __name__ == '__main__':
    unittest.main()
