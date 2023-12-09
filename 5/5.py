import math
from pathlib import Path
from typing import List, Tuple

import tqdm as tqdm

from util import load_txt_file_as_str, SubProblem

INPUT_FILE_PATH = Path("input_test_1")
SUB_PROBLEM = SubProblem.TWO


class Mapper:
    name: str
    map_values = List[Tuple[int, int, int]]

    def __init__(self, map_descriptor: List[str]):
        self.map_values = []
        self.name = map_descriptor.pop(0).replace(":", "")
        self._init_map_values(map_descriptor)

    def _init_map_values(self, range_descriptors: List[str]):
        for r_d in range_descriptors:
            dest_start, source_start, range_len = (int(value) for value in r_d.split(" "))
            self.map_values.append((source_start, dest_start - source_start, range_len))

        self.map_values = sorted(self.map_values)

        if self.map_values[0][0] != 0:
            self.map_values.insert(0, (0, 0, self.map_values[0][0]))

        self.map_values.append((self.map_values[-1][0] + self.map_values[-1][-1], 0, math.inf))

    def map_value(self, value: int) -> int:
        for idx, map_value in enumerate(self.map_values):
            if idx == len(self.map_values) - 1 or value < self.map_values[idx + 1][0]:
                return value + map_value[1]


def map_list_of_seeds(seeds: List[int]) -> List[int]:
    locations = []
    for seed in seeds:
        input = seed
        for mapper in mappers:
            input = mapper.map_value(input)

        locations.append(input)
    return locations


input_array = load_txt_file_as_str(INPUT_FILE_PATH).split("\n\n")
seeds = [int(value) for value in input_array.pop(0).replace("seeds: ", "").split(" ")]
map_array = [map.split("\n") for map in input_array]

mappers = [Mapper(map_descriptor) for map_descriptor in map_array]

if SUB_PROBLEM == SubProblem.ONE:
    locations = map_list_of_seeds(seeds)
    print(min(locations))

if SUB_PROBLEM == SubProblem.TWO:
    lowest_location = math.inf
    # seeds = [3037945983, 743948277]
    for idx in range(0, len(seeds), 2):
        seed_start = seeds[idx]
        range_number = seeds[idx + 1]
        # all_seeds_in_range = list(range(seed, seed + range_number))
        for seed in tqdm.tqdm(range(seed_start, seed_start + range_number)):
            location = map_list_of_seeds([seed])[0]
            if location < lowest_location:
                lowest_location = location

    print(lowest_location)

