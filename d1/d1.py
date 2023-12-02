from typing import List

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums_string = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def parse_input_file(path: str) -> List[str]:
    with open(path, "r") as input_file:
        input_list = input_file.readlines()

    return input_list


def main():
    input = parse_input_file(path="input.txt")

    sum = 0

    for row in input:
        idx_values_l = list()
        idx_values_r = list()

        for num_idx, num in enumerate(nums):
            idx_l = row.find(str(num))
            if idx_l != -1:
                idx_values_l.append((idx_l, num))

            idx_r = row.rfind(str(num))
            if idx_r != -1:
                idx_values_r.append((idx_r, num))

            idx_str_l = row.find(nums_string[num_idx])
            if idx_str_l != -1:
                idx_values_l.append((idx_str_l, num))

            idx_str_r = row.rfind(nums_string[num_idx])
            if idx_str_r != -1:
                idx_values_r.append((idx_str_r, num))

        if idx_values_l and idx_values_r:
            l = min(idx_values_l, key=lambda t: t[0])
            r = max(idx_values_r, key=lambda t: t[0])

            calibration_value = int(f"{l[1]}{r[1]}")
            sum += calibration_value

    print(sum)


if __name__ == '__main__':
    main()
