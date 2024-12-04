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


def parse_input_2(puzzle_input):
    pattern = re.compile(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))")
    return pattern.findall(puzzle_input)


def part_2(puzzle_input):
    matches = parse_input_2(puzzle_input)

    total = 0
    multiply_enabled = True
    for match in matches:
        if match == "do()":
            multiply_enabled = True
        elif match == "don't()":
            multiply_enabled = False
        elif match.startswith("mul("):
            if multiply_enabled:
                a, b = map(int, match[4:-1].split(","))
                total += a * b

    return total


def main():
    puzzle_input = get_puzzle_input(3).strip()
    print(f"{part_1(puzzle_input)=}")
    print(f"{part_2(puzzle_input)=}")


if __name__ == "__main__":
    main() 
