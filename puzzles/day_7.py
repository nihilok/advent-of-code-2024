import operator as op
from itertools import product

from aoc_utils import get_puzzle_input


def parse_input(puzzle_input):
    equations = puzzle_input.splitlines()
    parsed_equations = []
    for equation in equations:
        result, parts = equation.split(": ")
        parts = list(map(int, parts.split(" ")))
        parsed_equations.append((int(result), parts))
    return parsed_equations


def evaluate_combinations(values, operations):
    results = []

    for ops in product(operations, repeat=len(values) - 1):
        result = values[0]
        for i, operation in enumerate(ops):
            result = operation(result, values[i + 1])
        results.append(result)

    return results


def part_1(puzzle_input):
    equations = parse_input(puzzle_input)
    operations = [op.add, op.mul]
    total = 0
    for target, values in equations:
        results = evaluate_combinations(values, operations)
        if target in results:
            total += target
    return total


def part_2(puzzle_input):
    pass


def main():
    puzzle_input = get_puzzle_input(7).strip()
    print(f"{part_1(puzzle_input)=}")
    print(f"{part_2(puzzle_input)=}")


if __name__ == "__main__":
    main()
