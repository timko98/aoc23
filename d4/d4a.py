from input_handling import parse_input_file


def main():
    # input_file = parse_input_file("example.txt")
    input_file = parse_input_file("input.txt")

    sum_of_points = 0

    for card_idx, card in enumerate(input_file):
        winning_nums, my_nums = tuple(card.split(":")[1].split("|"))
        winning_nums = [int(x.strip()) for x in winning_nums.strip().split(" ") if x]
        my_nums = [int(x.strip()) for x in my_nums.strip().split(" ") if x]

        winning_nums_set = set(winning_nums)

        card_sum = 0

        for num in my_nums:
            if num in winning_nums_set:
                if card_sum == 0:
                    card_sum += 1
                else:
                    card_sum *= 2

        sum_of_points += card_sum

    print(sum_of_points)


if __name__ == "__main__":
    main()
