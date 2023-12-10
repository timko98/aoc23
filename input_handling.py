from typing import List


def parse_input_file(path: str) -> List[str]:
    content = []
    with open(path, "r") as input_file:
        for line in input_file:
            content.append(line.rstrip())

    return content
