""" Functionality for drawing the simulation state"""
import collections
import os
from typing import List, Dict

import robot


def _build_row_string(width: int, row_robot_characters: Dict[int, str]):
    """
    Build a string representing one row of the output grid. Any positions with
    robots are included in row_robot_characters, '.' is used for empty positions
    :param width: the width of the row
    :param row_robot_characters: a dictionary of {x: symbol} for all robots on
    this row
    :return: a string representing the row
    """
    return "".join([row_robot_characters.get(i, ".") for i in range(width)])


def _facing_symbol(robot):
    if robot.lost:
        return "X"
    facing = robot.facing
    if facing == "N":
        return "^"
    elif facing == "E":
        return ">"
    elif facing == "S":
        return "V"
    else:
        return "<"


def draw_state(grid_size, robots: List[robot.Robot]):
    w, h = grid_size
    # Build a dict of {y: {x: symbol}} for all robots where (x, y) is
    # the screen position for the robot, and symbol shows the direction it's
    # facing.
    robot_pos_characters = collections.defaultdict(dict)
    for r in robots:
        x, y = r.pos
        # We have to invert the y position because 0 represents the bottom of
        # the grid, but we draw it top down
        robot_pos_characters[h - y - 1][x] = _facing_symbol(r)

    grid = [_build_row_string(w, robot_pos_characters[i]) for i in range(h)]
    grid_str = "\n".join(grid)
    os.system("cls || clear")
    print(grid_str)
