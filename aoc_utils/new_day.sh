#!/usr/bin/env bash

DAY=$1

if [ -z $DAY ]; then
    echo "Usage: $0 <day>"
    exit 1
fi

CURRENT_DIR=$(pwd)

TEMPLATE='from aoc_utils import get_puzzle_input


def parse_input(puzzle_input):
    pass


def part_1(puzzle_input):
    pass


def part_2(puzzle_input):
    pass


def main():
    puzzle_input = get_puzzle_input('${DAY}').strip()
    print(f"{part_1(puzzle_input)=}")
    print(f"{part_2(puzzle_input)=}")


if __name__ == "__main__":
    main()
'

NEW_FILE="${CURRENT_DIR}/day_${DAY}.py"

echo "$TEMPLATE" > "${NEW_FILE}"
echo "Done! Created ${NEW_FILE}"
