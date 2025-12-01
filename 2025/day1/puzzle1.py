from pathlib import Path
from typing import Literal

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input1.txt")
SUB_PROBLEM = SubProblem.ONE

DIAL_START = 50
TOTAL_DIAL_STEPS = 100

def rotate_dial(start_position: int, direction: Literal["L", "R"], n_steps: int, total_dial_steps: int) -> tuple[int, int]:
    sign = -1 if direction == "L" else 1
    new_position_raw = start_position + sign * n_steps

    new_position = new_position_raw % total_dial_steps
    n_zero_passes = (int((start_position * new_position_raw) < 0) +
                     (abs(new_position_raw)) // total_dial_steps)

    if new_position == 0:
        n_zero_passes = max(0, n_zero_passes - 1)

    return new_position, n_zero_passes

def parse_input(rotation_input: str) -> tuple[str, int]:
    return rotation_input[0], int(rotation_input[1:])

def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
    start_position = DIAL_START

    end_zero_count = 0
    intermediate_zero_count = 0

    for rotation in input_array:
        direction, n_steps = parse_input(rotation)
        new_position, intermediate_zero_count_increment = (
            rotate_dial(start_position, direction, n_steps, TOTAL_DIAL_STEPS))
        end_zero_count += (new_position == 0)
        intermediate_zero_count += intermediate_zero_count_increment
        start_position = new_position

    print(end_zero_count)
    print(intermediate_zero_count)
    print(end_zero_count + intermediate_zero_count)

if __name__ == "__main__":
    main()
