from typing import Union

Facing = Union['N', 'E', 'S', 'W']
Turn = Union['L', 'R']
Command = Union[Turn, 'F']

_facings = ['N', 'E', 'S', 'W']


class Robot:
    pos: (int, int)
    facing: Facing
    lost = False
    commands: str
    next_command = 0

    def __init__(self, init_facing: Facing, init_pos: (int, int), commands: str):
        self.pos = init_pos
        self.facing = init_facing
        self.commands = commands

    def tick(self, grid_size: (int, int)):
        if not self.is_active():
            return

        command = self.commands[self.next_command]
        if command == 'F':
            next_position = _get_next_position(self.pos, self.facing)
            if out_of_bounds(next_position, grid_size):
                self.lost = True
                return

            self.pos = next_position
        else:
            self._turn(command)

        self.next_command += 1

    def _turn(self, direction: Turn):
        change = 1 if direction == 'R' else -1
        new_facing_index = (_facings.index(self.facing) + change) % len(_facings)
        self.facing = _facings[new_facing_index]

    def is_active(self):
        return not self.lost and self.next_command < len(self.commands)

    def output_state(self) -> str:
        state = f"({self.pos[0]}, {self.pos[1]}, {self.facing})"
        lost_str = " LOST" if self.lost else ""
        return f"{state}{lost_str}"

    def __str__(self) -> str:
        return f"Robot [pos: {self.pos}, " \
               f"facing: {self.facing}, " \
               f"lost: {self.lost}, " \
               f"commands: {self.commands}, " \
               f"next_command: {self.next_command}" \
               "]"


def _get_next_position(pos: (int, int), facing: Facing) -> (int, int):
    if facing == 'N':
        move = (0, 1)
    elif facing == 'E':
        move = (1, 0)
    elif facing == 'S':
        move = (0, -1)
    else:
        move = (-1, 0)

    return pos[0] + move[0], pos[1] + move[1]


def out_of_bounds(pos: (int, int), grid_size: (int, int)) -> bool:
    return pos[0] < 0 \
        or pos[1] < 0 \
        or pos[0] >= grid_size[0] \
        or pos[1] >= grid_size[1]
