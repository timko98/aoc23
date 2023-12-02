import math
from typing import List, Dict, Tuple


def parse_input_file(path: str) -> List[str]:
    with open(path, "r") as input_file:
        input_list = input_file.readlines()

    return input_list


def parse_game_string(game_string: str) -> Tuple[int, List[Dict[str, int]]]:
    id_string, games_string = game_string.split(":")[0], game_string.split(":")[1]
    games = list()

    for game in games_string.strip().split(";"):
        draws = game.strip().split(",")
        game_map = {}
        for draw in draws:
            game_map[draw.strip().split(" ")[1]] = int(draw.strip().split(" ")[0])

        games.append(game_map)

    return int(id_string.strip().split(" ")[1]), games


cube_configuration = {"red": 12, "green": 13, "blue": 14}


def main():
    input_list = parse_input_file(path="input.txt")

    sum = 0
    sum_of_power = 0

    for game_string in input_list:
        id, games = parse_game_string(game_string=game_string)

        min_cubes = {"red": 0, "green": 0, "blue": 0}

        possible = True

        for game in games:
            for cube, num in game.items():
                if cube_configuration[cube] < num:
                    possible = False

                if min_cubes[cube] < num:
                    min_cubes[cube] = num

        sum_of_power += math.prod(min_cubes.values())

        if possible:
            sum += id

    print(f"Sum of power {sum_of_power}")
    print(f"Sum {sum}")


if __name__ == '__main__':
    main()
