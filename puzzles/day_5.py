from collections import defaultdict

from aoc_utils import get_puzzle_input


def parse_input(puzzle_input):
    ordering, lines = puzzle_input.split("\n\n")
    ordering = ordering.splitlines()
    ordering = [tuple(row.split("|")) for row in ordering]
    pages_before = defaultdict(
        list
    )  # dict of pages where the value is a list of pages that must come before the key
    for before, after in ordering:
        pages_before[after].append(before)
    lines = lines.splitlines()
    lines = [line.split(",") for line in lines]
    return pages_before, lines


def part_1(puzzle_input):
    ordering, lines = parse_input(puzzle_input)
    total = 0 
    for line in lines:
        correct_order = True
        for i, page in enumerate(line):
            must_be_before = set(ordering[page])
            pages_after = set(line[i + 1 :])
            if must_be_before & pages_after:
                correct_order = False
                break
        if correct_order:
            middle_item = line[len(line) // 2]
            total += int(middle_item)
    return total


def part_2(puzzle_input):
    ordering, lines = parse_input(puzzle_input)
    total = 0
    for line in lines:
        for i, page in enumerate(line):
            
            def sort_key(x):
                # Couldn't make this work until I saw this insane solution: https://topaz.github.io/paste/#XQAAAQDaAAAAAAAAAAA5HUm7ztOXp5yfdseppGCV6GxFTkRHwUEPU3ig/49z0PbvEWzToWGuJkqTW5Cv8C47QBCn/Pj2JeQMaflTZA8TlrZwHHZ11OjQ0e8kdywged5S4r+xgrUyKH7cRwlxe3DPo3OZCyk6yBhQf0HhtQSuRWxuNA+7fQQIgJr1Ls/7un7PXYuEs+xti9+dUqKrJ0hq0amZ8hcPsdgnVz7gtii8OxEjKha4k3yQ+ET/wND/73ISZw==
                return -sum(x in ordering[page] for page in line)

            must_be_before = set(ordering[page])
            pages_after = set(line[i + 1 :])
            
            if must_be_before & pages_after:
                sorted_line = sorted(line, key=sort_key)
                middle_item = sorted_line[len(line) // 2]
                total += int(middle_item)
                break

    return total


def main():
    puzzle_input = get_puzzle_input(5).strip()
    print(f"{part_1(puzzle_input)=}")
    print(f"{part_2(puzzle_input)=}")


if __name__ == "__main__":
    main()
