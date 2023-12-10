from typing import List, Tuple


class Mapper:
    def __init__(self, mappings_as_list: List[List[int]]) -> None:
        self._ranges, self._mappers = self._create_mapping(mappings_as_list)

    def _create_mapping(self, mappings_as_list: List[List[int]]):
        ranges = []
        mappers = []

        for mapping in mappings_as_list:
            ranges.append((mapping[1], mapping[1] + mapping[2]))
            mappers.append(mapping[0] - mapping[1])

        return ranges, mappers

    def map(self, val: int) -> int:
        for idx, mapping_range in enumerate(self._ranges):
            if mapping_range[0] <= val <= mapping_range[1]:
                val += self._mappers[idx]
                return val
        return val

    def map_part_b(self, vals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        for input_idx, ranged_input in enumerate(vals):
            changed = False

            for mapping_idx, mapping_range in enumerate(self._ranges):
                if changed:
                    continue

                input_range = range(ranged_input[0], ranged_input[1])
                mapping_range = range(mapping_range[0], mapping_range[1])
                overlap = range(max(input_range[0], mapping_range[0]), min(input_range[-1], mapping_range[-1]) + 1)

                if len(overlap) == 0:
                    continue

                overlap_start = overlap[0]
                overlap_end = overlap[-1] + 1

                vals[input_idx] = (
                    overlap_start + self._mappers[mapping_idx],
                    overlap_end + self._mappers[mapping_idx],
                )

                if overlap_start > input_range[0]:
                    vals.append((ranged_input[0], overlap_start))

                if overlap_end < input_range[-1] + 1:
                    vals.append((overlap_end + 1, input_range[-1] + 1))

                changed = True

        return vals
