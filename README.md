# mars-rover

Simulates robots moving around a grid according to preprogrammed commands. Tested with python 3.10, should work with any 3.8+ version.

## Usage

```
python main.py [FILE] [OPTIONS]

ARGS:
    <FILE>
        The path to a file to read input from. If omitted, user will be
        prompted to enter values interactively

OPTIONS:
    -a, --animated
        Show the steps of the simulation

    -h, --help
        Display help information
```

The two examples from the brief are included in the `examples` folder - try them out with `python main.py examples/example-1` from this directory.

## Details

The simulation input can be provided in a file, or interactively. The first line of the input is the grid size, and any following lines are robots.

 - Grid size must be two positive integers separated by spaces
 - Robots must be in the format "(x, y, facing) commands", where x and y must be positive integers inside the grid size, facing is one of the chracters N, E, S, or W, and commands is a string made up of the characters L, R, and F.

When running, each robot will execute its commands in order until either there are none left, or the robot runs off of the grid. 'F' causes it to move in the direction it's facing, whilst 'L' and 'R' make it turn left and right respectively.

## Assumptions

I made a couple of assumptions that the brief didn't cover:

 - Robots can't collide (they're fine to occupy the same space).
 - In the first example, one robot ends up with x = 4 on a grid of width 4, despite the grid being 0 based. I assumed this was a mistake in the brief, this implementation instead has the robot become lost with x = 3 for it's final position.

## Extensions I didn't get to

 - A test suite - I only used the examples from the brief and some adhoc examples with manual testing.
 - Fixing types - the usage of Union types in `robot` doesn't actually work for static type checking; I was trying them out for the first time and hoped they'd work like union types from typescript. Using type hints was still handy for autocomplete suggestions, but I'd need to fix them to get their full utility.
 - Better error reporting on invalid inputs - it'd be useful to point out exactly where the input was invalid, and do it for _all_ lines in the file rather than just the first error. This would make the parsing logic quite a bit more complicated, however.
