from input_handling import parse_input_file

possible_cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1]

types = [[5], [1, 4], [2, 3], [1, 1, 3], [1, 2, 2], [1, 1, 1, 2], [1, 1, 1, 1, 1]][::-1]


def main():
    part_b = True
    input_file = parse_input_file("input.txt")
    # input_file = parse_input_file("example.txt")

    all_hands_and_bids = []

    for line in input_file:
        bid = int(line.split(" ")[1].strip())
        hand_val = int(map_hand_to_num(line.split(" ")[0].strip(), part_b))
        all_hands_and_bids.append((hand_val, bid))

    print(sorted(all_hands_and_bids))
    end_result = 0
    for idx, (_, bid) in enumerate(sorted(all_hands_and_bids)):
        end_result += (idx + 1) * bid

    print(end_result)


def map_hand_to_num(hand, part_b: bool = False):
    hand_val = ""

    hand_val += get_type(hand, part_b)

    for char in hand:
        char_val = str(possible_cards.index(char))
        if int(char_val) < 10:
            hand_val += f"0{char_val}"
        else:
            hand_val += str(possible_cards.index(char))

    return hand_val


def get_type(hand, part_b: bool):
    visited = []
    occurences = []
    for char in hand:
        if char in visited:
            continue
        occurences.append(hand.count(char))
        visited.append(char)

    occurences.sort()

    type_val = types.index(occurences) + 1

    if part_b and "J" in hand and type_val != 7:
        if type_val == 6:
            type_val = 7
        elif type_val == 5:
            type_val = 7
        elif type_val == 4:
            type_val = 6
        elif type_val == 3:
            if hand.count("J") == 2:
                type_val = 6
            else:
                type_val = 5
        elif type_val == 2:
            type_val = 4
        elif type_val == 1:
            type_val = 2

    return str(type_val)


if __name__ == "__main__":
    main()
