import parser


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
        grid_size, robots = parser.parse_lines(input_lines)
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
