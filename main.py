from typing import List
import sys

import parser
import robot


def read_interactive_input() -> ((int, int), List[robot.Robot]):
    """Interactively read the grid size and robots to run"""
    print("Welcome to mars rover. Input 'q' at any time to quit")
    grid_size = None
    while not grid_size:
        first = input(
            "Enter a grid size (two positive ints separated by whitespace): ")
        if first == "q":
            exit(0)

        try:
            grid_size = parser.parse_grid_size(first)
        except ValueError as ex:
            print(ex)

    robots = []
    while robot_line := input(
            "Enter a robot, or an empty line to run the simulation: "):
        if robot_line == "q":
            exit(0)

        try:
            r = parser.parse_robot(robot_line)
            if robot.out_of_bounds(r.pos, grid_size):
                raise ValueError("Robot would start out of bounds")
            robots.append(r)
            print("Robot added")
        except ValueError as ex:
            print(ex)

    return grid_size, robots


def read_input(args) -> ((int, int), List[robot.Robot]):
    """Read and parse input from specified file, or interactively if omitted"""
    if len(args) > 1:
        with open(args[1], "r") as f:
            try:
                return parser.parse_lines(f.readlines())
            except ValueError as ex:
                print(f"Input was invalid: {ex}")
                exit(1)
    else:
        return read_interactive_input()


def run(grid_size, robots):
    while any((r.is_active() for r in robots)):
        for r in robots:
            r.tick(grid_size)

    return [r.output_state() for r in robots]


if __name__ == '__main__':
    grid_size, robots = read_input(sys.argv)
    for result in run(grid_size, robots):
        print(result)
