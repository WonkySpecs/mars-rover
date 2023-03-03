from typing import List
import re
import robot


def parse_grid_size(line: str) -> (int, int):
    match = re.search(r"(\d+)\s+(\d+)", line)
    if not match:
        raise ValueError(f"{line} is not a valid grid size")
    return int(match.group(1)), int(match.group(2))


def parse_robot(line: str) -> robot.Robot:
    without_whitespace = line.replace(" ", "")
    match = re.search(r"\((\d+),(\d+),([NESW])\)([LRF]*$)", without_whitespace)
    if not match:
        raise ValueError(f"{line} is not a valid robot")
    pos = (int(match.group(1)), int(match.group(2)))
    return robot.Robot(match.group(3), pos, match.group(4))


def parse_lines(lines: List[str]) -> ((int, int), List[robot.Robot]):
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
