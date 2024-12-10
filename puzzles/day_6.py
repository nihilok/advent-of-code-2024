from typing import NamedTuple

from aoc_utils import get_puzzle_input

EXAMPLE_INPUT = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...\
"""

GUARD = "^"
OBSTRUCTION = "#"
MARKED = "X"


class Coordinate(NamedTuple):
    x: int
    y: int


class Directions(NamedTuple):
    UP: Coordinate = Coordinate(0, -1)
    RIGHT: Coordinate = Coordinate(1, 0)
    DOWN: Coordinate = Coordinate(0, 1)
    LEFT: Coordinate = Coordinate(-1, 0)


def parse_input(puzzle_input):
    return [list(line) for line in puzzle_input.splitlines()]


def create_path_to_next_obstacle(grid, direction):
    guard = next(
        Coordinate(x, y)
        for y, row in enumerate(grid)
        for x, position in enumerate(row)
        if position == GUARD
    )
    while True:
        next_position = Coordinate(guard.x + direction.x, guard.y + direction.y)
        try:
            if grid[next_position.y][next_position.x] == OBSTRUCTION:
                grid[guard.y][guard.x] = GUARD
                break
        except IndexError:
            grid[guard.y][guard.x] = MARKED
            raise StopIteration
        grid[guard.y][guard.x] = MARKED
        guard = next_position
    return grid


def create_path_with_stateful_grid(grid, direction):
    guard = next(map_position for row in grid for map_position in row if map_position.is_guard)
    while True:
        next_position = next(pos for row in grid for pos in row if pos.x == guard.x + direction.x and pos.y == guard.y + direction.y)
        if next_position.is_obstactle:
            break
        except StopIteration:
            break
        guard.is_guard = False
        guard.num_visits += 1
        next_position.is_guard = True
    all_visited_positions = [pos for pos in row for row in grid if pos.num_visits >= 2]




def part_1(puzzle_input):
    grid = parse_input(puzzle_input)
    directions = Directions()
    max_direction = len(directions)
    current_direction = directions.UP

    while True:
        try:
            grid = create_path_to_next_obstacle(grid, current_direction)
            current_direction = directions[
                (directions.index(current_direction) + 1) % max_direction
            ]
        except StopIteration:
            break

    return sum(position == MARKED for row in grid for position in row)


class MapPosition(NamedTuple):
    x: int
    y: int
    is_obstactle: bool
    is_guard: bool
    num_visits: int = 0

def part_2(puzzle_input):
    grid = parse_input(puzzle_input)
    stateful_grid = []
    for y, row in enumerate(grid):
        new_row = []
        for x, pos in enumerate(row):
            new_row.append(MapPosition(x=x, y=y, is_obstactle=pos==OBSTRUCTION, is_guard=pos==GUARD))
        stateful_grid.append(new_row)
    


def main():
    # puzzle_input = get_puzzle_input(6).strip()
    puzzle_input = EXAMPLE_INPUT.strip()
    print(f"{part_1(puzzle_input)=}")
    print(f"{part_2(puzzle_input)=}")


if __name__ == "__main__":
    main()
