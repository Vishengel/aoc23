from enum import Enum
from pathlib import Path
from typing import List, Union, Any


class SubProblem(Enum):
    ONE = "one"
    TWO = "two"


def load_txt_file_as_str(input_file: Path) -> str:
    with open(input_file) as input_file:
        input_str = input_file.read()

    return input_str


def load_txt_file_as_list_of_str(input_file: Path) -> List[str]:
    with open(input_file) as input_file:
        input_array = [line.replace("\n", "") for line in input_file.readlines()]

    return input_array


def load_txt_file_as_list_of_list_of_str(input_file: Path) -> List[List[str]]:
    with open(input_file) as input_file:
        input_array = [list(line.replace("\n", "")) for line in input_file.readlines()]

    return input_array


def is_out_of_bounds(input_array: Union[List[str], List[List]], x_pos: int, y_pos: int):
    """Check if coordinates in a 2D array are out of bounds
    """
    array_height = len(input_array)
    array_width = len(input_array[0])
    return x_pos < 0 or x_pos >= array_width or y_pos < 0 or y_pos >= array_height


def swap_list_elements(array: List[Any], idx1: int, idx2: int):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp
    return array
