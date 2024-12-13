from pathlib import Path
from typing import List, Tuple, Set

from util import load_txt_file_as_list_of_str, SubProblem, is_out_of_bounds

INPUT_FILE_PATH = Path("input0.txt")
SUB_PROBLEM = SubProblem.TWO

TOP_LEFT = (-1, -1)
TOP_RIGHT = (1, -1)
BOTTOM_LEFT = (-1, 1)
BOTTOM_RIGHT = (1, 1)

def cross_is_out_of_bounds(input_array, x, y):
    return (not is_out_of_bounds(input_array, x + TOP_LEFT[0], y + TOP_LEFT[1])
            and not is_out_of_bounds(input_array, x + BOTTOM_RIGHT[0], y + BOTTOM_RIGHT[1])) and (not is_out_of_bounds(input_array, x + BOTTOM_LEFT[0], y + BOTTOM_LEFT[1])
            and not is_out_of_bounds(input_array, x + TOP_RIGHT[0], y + TOP_RIGHT[1]))
def check_for_cross_words(input_array, x, y):
    if cross_is_out_of_bounds(input_array, x, y):
        return 0
    count = 0
    if (input_array[y + TOP_LEFT[1]][x + TOP_LEFT[0]] == "M" and input_array[y + BOTTOM_RIGHT[1]][
        x + BOTTOM_RIGHT[0]] == "S") or (
            input_array[y + TOP_LEFT[1]][x + TOP_LEFT[0]] == "S" and input_array[y + BOTTOM_RIGHT[1]][
        x + BOTTOM_RIGHT[0]] == "M"):
        ...

    if (not is_out_of_bounds(input_array, x + BOTTOM_LEFT[0], y + BOTTOM_LEFT[1])
            and not is_out_of_bounds(input_array, x + TOP_RIGHT[0], y + TOP_RIGHT[1])):
        if (input_array[y + BOTTOM_LEFT[1]][x + BOTTOM_LEFT[0]] == "M" and input_array[y + TOP_RIGHT[1]][
            x + TOP_RIGHT[0]] == "S") or (
                input_array[y + BOTTOM_LEFT[1]][x + BOTTOM_LEFT[0]] == "S" and input_array[y + TOP_RIGHT[1]][
            x + TOP_RIGHT[0]] == "M"):
            count += 1

    return count


def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)

    total_count = 0
    for y, row in enumerate(input_array):
        for x, letter in enumerate(row):
            if letter == "A":
                total_count += check_for_cross_words(input_array, x, y)

    print(total_count)


if __name__ == "__main__":
    main()
