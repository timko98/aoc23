from typing import Any

from mapper import Mapper


def parse_seeds_and_mappings(path: str, part_b: bool) -> Any:
    seeds = []
    mappers = []
    with open(path, "r") as input_file:
        mappings_as_list = []
        for line in input_file:
            if not line.strip():
                continue

            if line.startswith("seeds: "):
                seed_arguments = [int(x) for x in line.replace("seeds: ", "").strip().split(" ")]

                if not part_b:
                    seeds = seed_arguments
                    continue

                seeds = []
                for i in range(0, len(seed_arguments), 2):
                    start_idx = seed_arguments[i]
                    end_idx = start_idx + seed_arguments[i + 1]
                    seeds.append((start_idx, end_idx))

                continue

            if line.strip().endswith("map:"):
                if mappings_as_list:
                    mappers.append(Mapper(mappings_as_list=mappings_as_list))
                    mappings_as_list = []
                continue

            mappings_as_list.append([int(x) for x in line.strip().split(" ")])

    mappers.append(Mapper(mappings_as_list=mappings_as_list))
    return seeds, mappers


def main():
    part_b = True
    # seeds, mappers = parse_seeds_and_mappings("example.txt", part_b=part_b)
    seeds, mappers = parse_seeds_and_mappings("input.txt", part_b=part_b)

    for idx, mapper in enumerate(mappers):
        if not part_b:
            seeds = [mapper.map(x) for x in seeds]
        else:
            seeds = mapper.map_part_b(vals=seeds)

    print(seeds)
    print(min(seeds, key=lambda t: t[0])[0])


if __name__ == "__main__":
    main()
