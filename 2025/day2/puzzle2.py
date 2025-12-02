from functools import lru_cache
from pathlib import Path
from typing import Callable

from util import SubProblem, load_txt_file_as_str

INPUT_FILE_PATH = Path("input1.txt")
SUB_PROBLEM = SubProblem.TWO

def is_invalid_simple(id: str) -> bool:
    if (len(id) % 2) == 1:
        return False

    str_len = len(id)
    return id[:str_len // 2] == id[str_len // 2:]

def is_invalid_complex(id: str) -> bool:
    if len(id) == 1:
        return False

    if len(set(id)) == 1:
        # Case where one digit is repeated for the full length of the ID
        return True

    possible_sequence_sizes = get_possible_sequence_sizes(id)

    # Skip size == 1 as we've already checked that
    for size in possible_sequence_sizes[1:]:
        repeats = has_repeating_sequence_of_size_n(id, size)
        if repeats:
            return True

    return False

def get_possible_sequence_sizes(id: str) -> list[int]:
    # Absolutely degenerate list comprehension lmao
    return [idx for idx in range(1, (len(id) // 2) + 1) if (len(id) % len(id[:idx])) == 0]

def has_repeating_sequence_of_size_n(id: str, size: int) -> bool:
    split_indices = list(range(0, len(id)+1, size))
    id_splits = []

    for idx in range(len(split_indices) - 1):
        id_splits.append(id[split_indices[idx]:split_indices[idx+1]])

    return len(set(id_splits)) == 1

def find_invalid_ids_in_range(id_ranges: tuple[str, str], invalidity_function: Callable[[str], bool]) -> list[str]:
    invalid_ids = []
    range_start = int(id_ranges[0])
    range_end = int(id_ranges[1]) + 1

    for idx in range(range_start, range_end):
        if invalidity_function(str(idx)):
            invalid_ids.append(idx)

    return invalid_ids

def main():
    invalid_ids = []

    input_string = load_txt_file_as_str(INPUT_FILE_PATH)
    id_ranges = [(x.split("-")[0], x.split("-")[1]) for x in input_string.split(",")]

    invalidity_function = is_invalid_simple if SUB_PROBLEM == SubProblem.ONE else is_invalid_complex

    for id_range in id_ranges:
        invalid_ids.extend(find_invalid_ids_in_range(id_range, invalidity_function))

    print(invalid_ids)
    print(sum(invalid_ids))

if __name__ == "__main__":
    main()
