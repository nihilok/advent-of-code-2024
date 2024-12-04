from aoc_utils import get_puzzle_input

XMAS = "XMAS"
SAMX = "SAMX"


def parse_input(puzzle_input):
    return [
        [letter.upper() for letter in list(line)] for line in puzzle_input.splitlines()
    ]


def check_horizontal(grid):
    found = 0
    for row in grid:
        for i in range(len(row) - len(XMAS) + 1):
            check_word = "".join(row[i : i + len(XMAS)])
            if check_word == XMAS or check_word == SAMX:
                found += 1
    return found


def check_vertical(grid):
    found = 0
    for col in range(len(grid[0])):
        for row in range(len(grid) - len(XMAS) + 1):
            check_word = "".join(grid[row + i][col] for i in range(len(XMAS)))
            if check_word == XMAS or check_word == SAMX:
                found += 1
    return found


def check_diagonal(grid):
    found = 0
    height, width = len(grid), len(grid[0])
    for i in range(height - len(XMAS) + 1):
        for j in range(width - len(XMAS) + 1):
            check_word = "".join(grid[i + k][j + k] for k in range(len(XMAS)))
            if check_word == XMAS or check_word == SAMX:
                found += 1
    for i in range(len(XMAS) - 1, height):
        for j in range(width - len(XMAS) + 1):
            check_word = "".join(grid[i - k][j + k] for k in range(len(XMAS)))
            if check_word == XMAS or check_word == SAMX:
                found += 1
    return found


def part_1(puzzle_input):
    grid = parse_input(puzzle_input)
    return check_horizontal(grid) + check_vertical(grid) + check_diagonal(grid)


"""
PART 2
"""


PATTERN_1 = [
    ["M", ".", "S"],
    [".", "A", "."],
    ["M", ".", "S"],
]

PATTERN_2 = [
    ["S", ".", "M"],
    [".", "A", "."],
    ["S", ".", "M"],
]

PATTERN_3 = [
    ["M", ".", "M"],
    [".", "A", "."],
    ["S", ".", "S"],
]

PATTERN_4 = [
    ["S", ".", "S"],
    [".", "A", "."],
    ["M", ".", "M"],
]


def check_grid_for_pattern(grid, pattern):
    found = 0
    grid_len_y, grid_len_x = len(grid), len(grid[0])
    pattern_len_y, pattern_len_x = len(pattern), len(pattern[0])
    for i in range(grid_len_y - pattern_len_y + 1):
        for j in range(grid_len_x - pattern_len_x + 1):
            check = True
            for k in range(pattern_len_y):
                for l in range(pattern_len_x):
                    if pattern[k][l] != "." and pattern[k][l] != grid[i + k][j + l]:
                        check = False
                        break
                if not check:
                    break
            if check:
                found += 1
    return found


def part_2(puzzle_input):
    grid = parse_input(puzzle_input)
    return (
        check_grid_for_pattern(grid, PATTERN_1)
        + check_grid_for_pattern(grid, PATTERN_2)
        + check_grid_for_pattern(grid, PATTERN_3)
        + check_grid_for_pattern(grid, PATTERN_4)
    )


if __name__ == "__main__":
    DAY = 4
    puzzle_input = get_puzzle_input(DAY).strip()
    print(f"{part_1(puzzle_input)=}")
    print(f"{part_2(puzzle_input)=}")
