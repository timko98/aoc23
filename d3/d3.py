from typing import List, Optional, Tuple

from input_handling import parse_input_file

# input_file = parse_input_file("example.txt")
input_file = parse_input_file("input.txt")
handled = {}
max_col_idx = len(input_file[0]) - 1
max_row_idx = len(input_file) - 1


def main():
    riddle_part_b = True
    sum_engine = 0

    for row_idx, row in enumerate(input_file):
        for col_idx, col in enumerate(row):
            if not col.isalnum() and not col == ".":
                adjacent_nums = get_adjacent_nums(row_idx=row_idx, col_idx=col_idx)

                if adjacent_nums:
                    to_sum_list: List[int] = []

                    for num_row_idx, num_col_idx in adjacent_nums:
                        expanded_num = expand_num(row_idx=num_row_idx, col_idx=num_col_idx)

                        if expanded_num:
                            to_sum_list.append(expanded_num)

                    if not riddle_part_b:
                        sum_engine += sum(to_sum_list)
                        continue

                    if len(to_sum_list) == 2:
                        sum_engine += to_sum_list[0] * to_sum_list[1]
                    else:
                        continue

    print(sum_engine)


def expand_num(row_idx: int, col_idx: int) -> Optional[int]:
    orig_col_idx = col_idx

    if (row_idx, col_idx) in handled.keys():
        # already handled before
        return None
    else:
        num_string = input_file[row_idx][col_idx]

    while col_idx < max_col_idx and input_file[row_idx][col_idx + 1].isnumeric():
        num_string += input_file[row_idx][col_idx + 1]
        handled[(row_idx, col_idx + 1)] = "X"
        col_idx += 1

    col_idx = orig_col_idx
    while col_idx > 0 and input_file[row_idx][col_idx - 1].isnumeric():
        num_string = input_file[row_idx][col_idx - 1] + num_string
        handled[(row_idx, col_idx - 1)] = "X"
        col_idx -= 1

    # print(num_string)
    return int(num_string)


def get_adjacent_nums(row_idx: int, col_idx: int) -> Optional[List[Tuple[int]]]:
    adjacent_num_idx = []

    for possible_row in range(max(0, row_idx - 1), min(max_row_idx + 1, row_idx + 2)):
        for possible_col in range(max(0, col_idx - 1), min(max_col_idx + 1, col_idx + 2)):
            possible_num = input_file[possible_row][possible_col]
            if possible_num.isnumeric():
                adjacent_num_idx.append((possible_row, possible_col))

    return adjacent_num_idx


if __name__ == "__main__":
    main()
