from typing import List


def parse_input_file(path: str) -> List[str]:
    with open(path, "r") as input_file:
        input_list = input_file.readlines()

    return input_list
