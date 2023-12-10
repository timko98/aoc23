from input_handling import parse_input_file


def main():
    # input_file = parse_input_file("example.txt")
    input_file = parse_input_file("input.txt")

    total_scratchcards = len(input_file)
    num_scratchcards = [1 for x in range(total_scratchcards)]

    for card_idx, card in enumerate(input_file):
        winning_nums, my_nums = tuple(card.split(":")[1].split("|"))
        winning_nums = [int(x.strip()) for x in winning_nums.strip().split(" ") if x]
        my_nums = [int(x.strip()) for x in my_nums.strip().split(" ") if x]

        winning_nums_set = set(winning_nums)

        num_matches = 0

        for num in my_nums:
            if num in winning_nums_set:
                num_matches += 1

        if num_matches == 0:
            continue

        start_idx = card_idx + 1
        end_idx = card_idx + num_matches
        num_copies = num_scratchcards[card_idx]
        num_scratchcards[start_idx : end_idx + 1] = [
            x + (1 * num_copies) for x in num_scratchcards[start_idx : end_idx + 1]
        ]

    print(sum(num_scratchcards))


if __name__ == "__main__":
    main()
