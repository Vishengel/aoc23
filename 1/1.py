from pathlib import Path
from typing import Optional, List

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input")
SUB_PROBLEM = SubProblem.TWO
WRITTEN_DIGIT_MAPPING = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                         "eight": "8", "nine": "9"}


def add_written_digits(input_string: str) -> str:
    for written_digit in WRITTEN_DIGIT_MAPPING:
        input_string = input_string.replace(written_digit, written_digit + WRITTEN_DIGIT_MAPPING[written_digit] +
                                            written_digit[-1])

    return input_string


def find_first_digit_in_string(input_string: str) -> Optional[str]:
    char = None
    for char in input_string:
        if char.isdigit():
            return char

    return char


def get_calibration_values(input_array: List[str]) -> List[str]:
    return [find_first_digit_in_string(input_string) + find_first_digit_in_string(input_string[::-1])
            for input_string in input_array]


input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)

if SUB_PROBLEM == SUB_PROBLEM.TWO:
    input_array = [add_written_digits(input_string) for input_string in input_array]

calibration_values = get_calibration_values(input_array)
calibration_sum = sum([int(val) for val in calibration_values])
print(calibration_sum)
