from collections import deque
from dataclasses import dataclass

from aoc_utils import get_puzzle_input

example_1 = "12345"
example_2 = "2333133121414131402"


@dataclass
class FileBlock:
    file_id: int

    def __repr__(self):
        return str(self.file_id)


class FileSystem(list):
    def __repr__(self):
        return "".join(repr(b) if b is not None else "." for b in self)


def parse_input(puzzle_input):
    file_id = 0
    initial_disk = FileSystem()
    for i, n in enumerate(puzzle_input):
        size = int(n)
        if not i % 2:
            initial_disk.extend([FileBlock(file_id=file_id)] * size)
            file_id += 1
        else:
            initial_disk.extend([None] * size)
    return initial_disk


def part_1(puzzle_input):
    initial = parse_input(puzzle_input)
    compacted = False
    while not compacted:
        print(initial)
        for i, block in enumerate(initial):
            compacted = all((b is None for b in initial[i:]))
            if block is None:
                for j, end_block in enumerate(reversed(initial)):
                    if end_block is not None:
                        print(end_block)
                        initial[i] = end_block
                        initial[-j] = None
                        break
                break

    return repr_deque(initial)


def part_2(puzzle_input):
    pass


def main():
    # puzzle_input = get_puzzle_input(9).strip()
    puzzle_input = example_1
    print(f"{part_1(puzzle_input)=}")
    print(f"{part_2(puzzle_input)=}")


if __name__ == "__main__":
    main()
