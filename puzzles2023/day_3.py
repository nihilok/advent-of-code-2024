"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""

from string import punctuation
from aoc_utils import get_puzzle_input

symbols = [s for s in punctuation if s != "."]

def is_part_number(data, line_index, number_start, number_end):
    current_line = data[line_index]

    # Check symbols in current line
    if number_start > 0 and current_line[number_start - 1] in symbols:
        return True
    if number_end < len(current_line) - 1 and current_line[number_end + 1] in symbols:
        return True

    # Check symbols in the line above
    if line_index > 0:
        previous_line = data[line_index - 1]
        if any(c in symbols for c in previous_line[number_start:number_end + 1]):
            return True

    # Check symbols in the line below
    if line_index < len(data) - 1:
        next_line = data[line_index + 1]
        if any(c in symbols for c in next_line[number_start:number_end + 1]):
            return True

    return False

def part_1(data):
    data = data.split("\n")
    part_numbers = []
    for line_index, line in enumerate(data):
        num_start = None
        for i, c in enumerate(line):
            if c.isnumeric():
                if num_start is None:
                    num_start = i
            else:
                if num_start is not None:
                    num_end = i - 1
                    if is_part_number(data, line_index, num_start, num_end):
                        part_numbers.append(int(line[num_start:num_end + 1]))
                    num_start = None
        # Check if a number continues till the end of the line
        if num_start is not None:
            num_end = len(line) - 1
            if is_part_number(data, line_index, num_start, num_end):
                part_numbers.append(int(line[num_start:num_end + 1]))
    return sum(part_numbers)

if __name__ == "__main__":
    puzzle_input = get_puzzle_input(day=3, year=2023)
    print("Part 1 Answer:", part_1(puzzle_input))
