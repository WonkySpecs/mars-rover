import argparse
import time
from typing import List

import output
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


def read_input(file_name) -> ((int, int), List[robot.Robot]):
    """Read and parse input from specified file, or interactively if omitted"""
    if file_name:
        with open(file_name, "r") as f:
            try:
                return parser.parse_lines(f.readlines())
            except ValueError as ex:
                print(f"Input was invalid: {ex}")
                exit(1)
    else:
        return read_interactive_input()


def run(grid_size, robots, animated=False):
    while any((r.is_active() for r in robots)):
        for r in robots:
            r.tick(grid_size)

        if animated:
            output.draw_state(grid_size, robots)
            time.sleep(0.3)

    return [r.output_state() for r in robots]


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        prog="Mars Rover",
        description="Simulate programmed robots moving around a grid. See the "
                    "examples folder for examples of the input format",
    )
    arg_parser.add_argument(
        "filename",
        nargs="?",
        help="The file to read simulation input from. If omitted, input will "
             "be read interactively.")
    arg_parser.add_argument(
        "-a", "--animated",
        action="store_true",
        help="Display the steps of the simulation")
    args = arg_parser.parse_args()

    grid_size, robots = read_input(args.filename)
    for result in run(grid_size, robots, animated=args.animated):
        print(result)
