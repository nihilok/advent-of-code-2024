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


def checksum(fs):
    total = 0
    for i, block in enumerate(fs):
        if block is None:
            break
        total += i * int(block.file_id)
    return total


def part_1(puzzle_input):
    initial = parse_input(puzzle_input)
    backup = initial.copy()
    compacted = False
    end_fs = FileSystem()
    for i, start_block in enumerate(initial):
        if i >= len(backup):
            break
        if start_block is not None:
            end_fs.append(start_block)
        else:

            for _ in range(len(backup)):
                end_block = backup.pop()
                if end_block is not None:
                    end_fs.append(end_block)
                    break
    # end_fs.extend([None] * (len(initial) - len(end_fs)))
    return checksum(end_fs)


def part_2(puzzle_input):
    pass


def main():
    puzzle_input = get_puzzle_input(9).strip()
    # puzzle_input = example_2
    print(f"{part_1(puzzle_input)=}")
    print(f"{part_2(puzzle_input)=}")


if __name__ == "__main__":
    main()
