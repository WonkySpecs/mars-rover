# mars-rover

Simulates robots moving around a grid according to preprogrammed commands. Tested with python 3.10, should work with any 3.8+ version.

## Usage

```
python main.py [FILE]

ARGS:
    <FILE>
        The path to a file to read an input for. If omitted, user will be
        prompted to enter values interactively
```

The two examples from the brief are included in the `examples` folder - try them out with `python main.py examples/example-1` from this directory.

## Details

The simulation input can be provided in a file, or interactively. The first line of the input is the grid size, and any following lines are robots.

 - Grid size must be two positive integers separated by spaces
 - Robots must be in the format "(x, y, facing) commands", where x and y must be positive integers inside the grid size, facing is one of the chracters N, E, S, or W, and commands is a string made up of the characters L, R, and F.

When running, each robot will execute its commands in order until either there are none left, or the robot runs off of the grid. 'F' causes it to move in the direction it's facing, whilst 'L' and 'R' make it turn left and right respectively.
