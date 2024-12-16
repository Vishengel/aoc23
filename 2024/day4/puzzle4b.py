from pathlib import Path

from util import load_txt_file_as_list_of_str, SubProblem, is_out_of_bounds

INPUT_FILE_PATH = Path("input1.txt")
SUB_PROBLEM = SubProblem.TWO

TOP_LEFT = (-1, -1)
TOP_RIGHT = (1, -1)
BOTTOM_LEFT = (-1, 1)
BOTTOM_RIGHT = (1, 1)


def cross_is_out_of_bounds(input_array, x, y) -> bool:
    return is_out_of_bounds(input_array, x + TOP_LEFT[0], y + TOP_LEFT[1]) or \
        is_out_of_bounds(input_array, x + BOTTOM_RIGHT[0], y + BOTTOM_RIGHT[1]) or \
        is_out_of_bounds(input_array, x + BOTTOM_LEFT[0], y + BOTTOM_LEFT[1]) or \
        is_out_of_bounds(input_array, x + TOP_RIGHT[0], y + TOP_RIGHT[1])


def check_for_cross_words(input_array, x, y) -> bool:
    if cross_is_out_of_bounds(input_array, x, y):
        return False

    top_left_bottom_right = False

    if input_array[y + TOP_LEFT[1]][x + TOP_LEFT[0]] == "M":
        if input_array[y + BOTTOM_RIGHT[1]][x + BOTTOM_RIGHT[0]] == "S":
            top_left_bottom_right = True
    elif input_array[y + TOP_LEFT[1]][x + TOP_LEFT[0]] == "S":
        if input_array[y + BOTTOM_RIGHT[1]][x + BOTTOM_RIGHT[0]] == "M":
            top_left_bottom_right = True

    top_right_bottom_left = False

    if input_array[y + TOP_RIGHT[1]][x + TOP_RIGHT[0]] == "M":
        if input_array[y + BOTTOM_LEFT[1]][x + BOTTOM_LEFT[0]] == "S":
            top_right_bottom_left = True
    elif input_array[y + TOP_RIGHT[1]][x + TOP_RIGHT[0]] == "S":
        if input_array[y + BOTTOM_LEFT[1]][x + BOTTOM_LEFT[0]] == "M":
            top_right_bottom_left = True

    return top_left_bottom_right and top_right_bottom_left


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
