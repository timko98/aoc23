import math


def parse_race_input(path: str, part_b: bool = False):
    times = []
    distances = []
    with open(path, "r") as input_file:
        for line in input_file:
            if line.startswith("Time:"):
                times = [int(x.strip()) for x in line.replace("Time:", "").strip().split(" ") if x]
            if line.startswith("Distance:"):
                distances = [int(x.strip()) for x in line.replace("Distance:", "").strip().split(" ") if x]

    if part_b:
        time = int("".join([str(time_val) for time_val in times]))
        distance = int("".join([str(dist_val) for dist_val in distances]))
        return [(time, distance)]
    return list(zip(times, distances))


def main():
    # time_distances = parse_race_input("example.txt", part_b=True)
    time_distances = parse_race_input("input.txt", part_b=True)
    print(time_distances)

    winning_conditions = list()
    # x^2 - tx + d = 0
    # -(p/2) +- sqrt((p/2)**2 - q)
    for t, d in time_distances:
        p = -t
        q = d + 1
        time_1 = math.floor(-p / 2 + math.sqrt((p / 2) ** 2 - q))
        time_2 = math.ceil(-p / 2 - math.sqrt((p / 2) ** 2 - q))

        winning_conditions.append(time_1 - time_2 + 1)

    print(math.prod(winning_conditions))


if __name__ == "__main__":
    main()
