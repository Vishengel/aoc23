from enum import Enum
from pathlib import Path
from typing import List


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
