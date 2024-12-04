from aoc_utils import get_puzzle_input


def parse_input(puzzle_input):
    reports = [[int(v) for v in line.split()] for line in puzzle_input.splitlines()]
    return reports


def is_safe_report(report):
    last_value = None
    ascending = None
    safe = True
    for value in report:
        if last_value is None:
            last_value = value
            continue
        if last_value == value:
            safe = False
            break
        if abs(last_value - value) > 3:
            safe = False
            break
        if ascending is True and last_value > value:
            safe = False
            break
        if ascending is False and last_value < value:
            safe = False
            break
        if ascending is None:
            ascending = last_value < value

        last_value = value
    return safe


def part_1(puzzle_input):
    reports = parse_input(puzzle_input)
    safe_reports = 0
    for report in reports:
        if is_safe_report(report):
            safe_reports += 1
    return safe_reports


def part_2(puzzle_input):
    reports = parse_input(puzzle_input)
    safe_reports = 0
    for report in reports:
        if is_safe_report(report):
            safe_reports += 1
            continue
        for i, value in enumerate(report):
            new_report = report.copy()
            new_report.pop(i)
            if is_safe_report(new_report):
                safe_reports += 1
                break
    return safe_reports


def main():
    puzzle_input = get_puzzle_input(2).strip()
    print(f"{part_1(puzzle_input)=}")
    print(f"{part_2(puzzle_input)=}")

if __name__ == "__main__":
    main() 
