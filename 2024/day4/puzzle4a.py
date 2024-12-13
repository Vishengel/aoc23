from pathlib import Path
from typing import List, Tuple, Set

from util import load_txt_file_as_list_of_str, SubProblem, is_out_of_bounds

INPUT_FILE_PATH = Path("input1.txt")
SUB_PROBLEM = SubProblem.ONE

WORD = "XMAS"
UP = {(-1, -1), (0, -1), (1, -1)}
RIGHT = {(1, -1), (1, 0), (1, 1)}
DOWN = {(-1, 1), (0, 1), (1, 1)}
LEFT = {(-1, -1), (-1, 0), (-1, 1)}
ALL_DIRECTIONS = UP | RIGHT | DOWN | LEFT  # Union of the four sets


def get_neighbor_coords(cur_x: int, cur_y: int, input_array: List[str]) -> Set[Tuple[int, int]]:
    array_height = len(input_array)
    array_width = len(input_array[0])

    neighbors = ALL_DIRECTIONS.copy()

    # Subtract all directions that are out of bounds
    if cur_y == 0:
        neighbors -= UP
    if cur_x == array_width - 1:
        neighbors -= RIGHT
    if cur_y == array_height - 1:
        neighbors -= DOWN
    if cur_x == 0:
        neighbors -= LEFT

    return {(cur_x + x_inc, cur_y + y_inc) for (x_inc, y_inc) in neighbors}


def follow_letters_all_directions(input_array: List[str], cur_x: int, cur_y: int, cur_letter_idx: int, count: int):
    """This was my first solution, because I misunderstood the assignment: I thought that the word could change
    direction multiple times, like a snake, instead of having to follow a straight line in any direction.
    """
    assert input_array[cur_y][cur_x] == WORD[cur_letter_idx]  # Sanity check

    if cur_letter_idx == len(WORD) - 1:
        # We've reached the last letter in the word
        return count + 1

    neighbor_coords = get_neighbor_coords(cur_x, cur_y, input_array)
    for (new_x, new_y) in neighbor_coords:
        if input_array[new_y][new_x] == WORD[cur_letter_idx + 1]:
            count = follow_letters_all_directions(input_array, new_x, new_y, cur_letter_idx + 1, count)

    return count


def follow_letters_straight_line(input_array: List[str], cur_x: int, cur_y: int, x_inc: int, y_inc: int,
                                 cur_letter_idx: int):
    if is_out_of_bounds(input_array, cur_x, cur_y) or input_array[cur_y][cur_x] != WORD[cur_letter_idx]:
        return 0

    if input_array[cur_y][cur_x] == WORD[-1]:
        return 1

    return follow_letters_straight_line(input_array, cur_x + x_inc, cur_y + y_inc, x_inc, y_inc,
                                        cur_letter_idx=cur_letter_idx + 1)


def check_for_word_in_all_directions(input_array, x, y):
    count = 0
    for (x_inc, y_inc) in ALL_DIRECTIONS:
        count += follow_letters_straight_line(input_array, x + x_inc, y + y_inc, x_inc, y_inc,
                                              cur_letter_idx=1)
    return count


def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)

    total_count = 0
    for y, row in enumerate(input_array):
        for x, letter in enumerate(row):
            if letter == WORD[0]:
                total_count += check_for_word_in_all_directions(input_array, x, y)

    print(total_count)


if __name__ == "__main__":
    main()
