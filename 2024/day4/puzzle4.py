from pathlib import Path
from typing import List, Tuple

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input0.txt")
SUB_PROBLEM = SubProblem.ONE

WORD = "XMAS"


def get_neighbor_coords(cur_x: int, cur_y: int) -> List[Tuple[int, int]]:
    ...


def follow_letters(input_array: List[str], cur_x: int, cur_y: int, next_letter_idx: int, count: int):
    ...

def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)

    total_count = 0
    for y, row in enumerate(input_array):
        for x, letter in enumerate(row):
            if letter == "X":
                total_count += follow_letters(input_array, x, y, 1, 0)

    print(total_count)


if __name__ == "__main__":
    main()
