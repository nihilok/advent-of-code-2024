import re
from aoc_utils import get_puzzle_input


def parse_input(puzzle_input):
    mul_pattern = re.compile(r"(mul\(\d{1,3},\d{1,3}\))") 
    muls = mul_pattern.findall(puzzle_input)
    return muls


def part_1(puzzle_input):
    muls = parse_input(puzzle_input)
    total = 0
    for mul in muls:
        a, b = map(int, mul[4:-1].split(","))
        total += a * b
    return total
        

def part_2(puzzle_input):
    pass


if __name__ == "__main__":
    DAY = 3
    puzzle_input = get_puzzle_input(DAY).strip()
    print(f"{part_1(puzzle_input)=}")
    print(f"{part_2(puzzle_input)=}")
