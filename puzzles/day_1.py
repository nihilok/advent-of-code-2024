from collections import Counter

from aoc_utils import get_puzzle_input


def parse(data):
    lines = data.splitlines()
    left, right = [], []
    for line in lines:
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))
    return left, right


def part_1(data):
    left, right = parse(data)
    total = 0
    while left and right:
        min_left = min(left)
        min_right = min(right)
        total += abs(min_left - min_right)
        left.remove(min_left)
        right.remove(min_right)
    return total


def part_2(data):
    left, right = parse(data)
    total = 0
    right_counter = Counter(right)
    for l in left:
        multiplier = right_counter.get(l, 0)
        total += l * multiplier
    return total


def main():
    puzzle_input = get_puzzle_input(day=1, year=2024)
    print(f"{part_1(puzzle_input)=}")
    print(f"{part_2(puzzle_input)=}")


if __name__ == "__main__":
    main()
