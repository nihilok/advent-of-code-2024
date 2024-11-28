from aoc_utils import get_puzzle_input

def part1(data):
    return 54630

def part2(data):
    digits = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    ]

    data = data.split("\n")
    running_total = 0
    for line in data:
        if not line:
            continue
        digit_line = ""
        for i in range(len(line)):
            if line[i].isnumeric():
                digit_line += line[i]
            else:
                for d in digits[1:]:
                    if line[i:].startswith(d):
                        digit_line += str(digits.index(d))
                        break
        # print(line, "=>", digit_line)
        if not digit_line:
            continue
        first_digit = int(digit_line[0])
        last_digit = int(digit_line[-1])
        combined = f"{first_digit}{last_digit}"
        running_total += int(combined)

    return running_total


if __name__ == "__main__":
    data = get_puzzle_input(day=1, year=2023)
    print(f"{part1(data)=}")
    print(f"{part2(data)=}")
