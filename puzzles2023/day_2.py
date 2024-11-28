from aoc_utils import get_puzzle_input
from collections import defaultdict

def part_1(data):
    games = data.split("\n")
    possible_games = []
    running_total = 0
    for game in games:
        if ":" not in game:
            continue
        game_name, game_data = game.split(": ")
        game_id = int(game_name.replace("Game ", ""))
        game_data = game_data.replace(";", ",")
        game_data = [(int(num), colour) for num, colour in [d.split(" ") for d in game_data.split(", ")]]
        possible = True
        for num, colour in game_data:
            if colour == "red" and num > 12:
                possible = False
            if colour == "blue" and num > 14:
                possible = False
            if colour == "green" and num > 13:
                possible = False
        if possible:
            possible_games.append(game_id)
    return sum(possible_games)



def part_2(data):
    games = data.split("\n")
    running_total = 0
    for game in games:
        if ":" not in game:
            continue
        game_name, game_data = game.split(": ")
        game_id = int(game_name.replace("Game ", ""))
        game_data = game_data.replace(";", ",")
        game_data = [(int(num), colour) for num, colour in [d.split(" ") for d in game_data.split(", ")]]
        max_drawn = defaultdict(int)
        for num, colour in game_data:
            max_drawn[colour] = max(max_drawn[colour], num)
        minimum_set_power = max_drawn["red"] * max_drawn["blue"] * max_drawn["green"]
        running_total += minimum_set_power
    return running_total



if __name__ == "__main__":
    data = get_puzzle_input(day=2, year=2023)
    part_1_answer = part_1(data)
    print(f"Part 1: {part_1_answer}")
    part_2_answer = part_2(data)
    print(f"Part 2: {part_2_answer}")
