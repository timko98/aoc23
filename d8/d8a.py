from input_handling import parse_input_file


def main():
    input_file = parse_input_file("input.txt")
    # input_file = parse_input_file("example.txt")
    # input_file = parse_input_file("example2.txt")

    directions = input_file[0]

    mapper = {}

    for line in input_file[2:]:
        key_and_directions = line.split("=")
        directions_list = key_and_directions[1].strip().replace("(", "").replace(")", "").split(",")

        mapper[key_and_directions[0].strip()] = directions_list[0].strip(), directions_list[1].strip()

    curr_el = "AAA"
    num_steps = 0
    found = False

    while not found:
        for char in directions:
            if char == "L":
                curr_el = mapper.get(curr_el)[0]
            elif char == "R":
                curr_el = mapper.get(curr_el)[1]

            num_steps += 1

            if curr_el == "ZZZ":
                found = True
                break

    print(num_steps)


if __name__ == "__main__":
    main()
