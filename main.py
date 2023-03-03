from typing import List

import parser
import robot


def read_input() -> ((int, int), List[robot.Robot]):
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


def run():
    input_lines = [
        "4 8",
        "(2, 3, E) LFRFF",
        "(0, 2, N) FFLFRFF"
    ]
    # input_lines = [
    #     "4 8",
    #     "(2, 3, N) FLLFR",
    #     "(1, 0, S) FFRLF"
    # ]
    try:
        # grid_size, robots = parser.parse_lines(input_lines)
        grid_size, robots = read_input()
    except ValueError as ex:
        print(f"Input was invalid: {ex}")
        exit(1)

    while any((r.is_active() for r in robots)):
        for r in robots:
            r.tick(grid_size)

    return [r.output_state() for r in robots]


if __name__ == '__main__':
    for result in run():
        print(result)
