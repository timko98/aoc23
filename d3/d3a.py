from input_handling import parse_input_file


def main():
    input_file = parse_input_file("example.txt")
    # input_file = parse_input_file("input.txt")

    for row in input_file:
        print(row)


if __name__ == "__main__":
    main()
