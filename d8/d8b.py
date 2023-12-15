from input_handling import parse_input_file


def main():
    input_file = parse_input_file("input.txt")
    input_file = parse_input_file("exampleb.txt")

    directions = input_file[0]

    starting_nodes = list()
    mapper = {}

    for line in input_file[2:]:
        key_and_directions = line.split("=")
        directions_list = key_and_directions[1].strip().replace("(", "").replace(")", "").split(",")

        key = key_and_directions[0].strip()
        if key.endswith("A"):
            starting_nodes.append(key)

        mapper[key] = directions_list[0].strip(), directions_list[1].strip()

    num_steps = 0
    found = False

    while not found:
        for char in directions:
            for idx, node in enumerate(starting_nodes):
                if char == "L":
                    starting_nodes[idx] = mapper.get(node)[0]
                elif char == "R":
                    starting_nodes[idx] = mapper.get(node)[0]

            num_steps += 1

            if not False in [node.endswith("Z") for node in starting_nodes]:
                found = True
                break

    print(num_steps)


if __name__ == "__main__":
    main()
