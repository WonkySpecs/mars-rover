import re
from typing import List

import robot


def parse_grid_size(line: str) -> (int, int):
    """
    Parses a string in the form "<x> <y>" into a pair of ints.

    x and y must be positive integers, extra whitespace is ignored.

    :param line: the line of input to parse as a grid size
    :return: the grid size, if the input was valid
    :raises ValueError: if the line does not match the required format
    """
    match = re.search(r"(\d+)\s+(\d+)", line)
    if not match:
        raise ValueError(f"{line} is not a valid grid size")
    return int(match.group(1)), int(match.group(2))


def parse_robot(line: str) -> robot.Robot:
    """
    Parses a string in the form "(<x>, <y>, <facing>) <commands>" as a robot.

    x and y must be positive integers, facing is one of the letters N, E,
    S or W, and commands is a string consisting of the letters L, R, and F.

    Whitespace is ignored
    :param line: the line of input to parse as a robot
    :return: a robot, if the line is valid
    :raises ValueError: if the line does not match the required format
    """
    without_whitespace = line.replace(" ", "")
    match = re.search(r"\((\d+),(\d+),([NESW])\)([LRF]*$)", without_whitespace)
    if not match:
        raise ValueError(f"{line} is not a valid robot")
    pos = (int(match.group(1)), int(match.group(2)))
    return robot.Robot(match.group(3), pos, match.group(4))


def parse_lines(lines: List[str]) -> ((int, int), List[robot.Robot]):
    """
    Parse a set of lines to get a grid size and list of robots.

    Ignores empty lines.
    :param lines: the lines of input to parse
    :return: the grid size and a list of robots to run
    :raises ValueError: if any part of input is invalid
    """
    grid_size = None
    robots = []
    for line in lines:
        # Skip blank lines
        if not line or not line.strip():
            continue

        # First non-blank line is the grid size, others are robots
        if not grid_size:
            grid_size = parse_grid_size(line)
        else:
            r = parse_robot(line)
            if robot.out_of_bounds(r.pos, grid_size):
                raise ValueError(f"Robot {line} starts out of bounds")
            robots.append(r)

    if not grid_size:
        raise ValueError("Grid size must be provided")

    return grid_size, robots
