from string import punctuation
from aoc_utils import get_puzzle_input

symbols = [s for s in punctuation if s != "."]

def is_part_number(data, line_index, number_start, number_end):
    current_line = data[line_index]
    
    if number_start > 0:
        slice_start = number_start - 1
    else:
        slice_start = 0

    if number_end < len(current_line) - 2:
        slice_end = number_end + 1
    else:
        slice_end = len(current_line) - 1
    
    if current_line[slice_start] in symbols:
        return True
    if current_line[slice_end] in symbols:
        return True
    
    previous_line = "NO PREVIOUS LINE"
    next_line = "NO NEXT LINE"
    section_above = ""
    section_below = ""

    if line_index > 0:
        previous_line = data[line_index - 1]
    
        section_above = previous_line[slice_start:slice_end + 1]

        for c in section_above:
            if c in symbols:
                return True
    
    if line_index < len(data) - 2:
        next_line = data[line_index + 1]

        section_below = next_line[slice_start:slice_end + 1]

        for c in section_below:
            if c in symbols:
                return True

    print("======NOT A PART NUMBER======")
    print(slice_start, slice_end)
    print(previous_line)
    print(current_line)
    print(next_line)
    print(section_above)
    print(current_line[number_start:number_end + 1])
    print(section_below)
    return False


def part_1(data):
    data = data.split("\n")
    part_numbers = []
    for line_index, line in enumerate(data):
        num_start = None
        num_end = None
        in_number = False
        for i, c in enumerate(line):
            if in_number and c.isnumeric():
                continue

            if in_number and not c.isnumeric():
                in_number = False
                num_end = i - 1
                if is_part_number(data, line_index, num_start, num_end):
                    part_numbers.append(int(line[num_start:num_end + 1]))
                
            if not in_number and c.isnumeric():
                num_start = i
                in_number = True
    return sum(part_numbers)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(day=3, year=2023)
    print("Part 1 Answer:", part_1(puzzle_input))
