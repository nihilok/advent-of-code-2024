#!/usr/bin/env bash

set -euo pipefail

DAY=$1

if [ -z $DAY ]; then
    echo "Usage: $0 <day>"
    exit 1
fi

CURRENT_DIR="$PWD"

if ! ls "puzzles" > /dev/null 2>&1; then
        if [ $(basename "$CURRENT_DIR") == "aoc_utils" ]; then
                CURRENT_DIR="../puzzles"
                if ! ls "$CURRENT_DIR" > /dev/null 2>&1; then
                        echo "No 'puzzles/' dir in project; exiting without creating file" && exit 1
                fi
        elif [ $(basename "$CURRENT_DIR") != "puzzles" ]; then
                echo "Must be run inside advent-of-code dir" && exit 1
        fi
else
        CURRENT_DIR="$CURRENT_DIR/puzzles"
fi      

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
echo "Created ${NEW_FILE}"

$EDITOR "$NEW_FILE" && exit 0 || echo "Error opening default editor" && exit 1

