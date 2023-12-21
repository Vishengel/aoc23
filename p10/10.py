from enum import Enum
from pathlib import Path

from util import SubProblem, load_txt_file_as_str

INPUT_FILE_PATH = Path("input_test_1")
SUB_PROBLEM = SubProblem.ONE


class Direction(Enum):
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"


SYMBOL_TO_PIPE_MAP = {"|": (Direction.NORTH, Direction.SOUTH), "-": (Direction.EAST, Direction.WEST),
                      "L": (Direction.NORTH, Direction.EAST), "J": (Direction.NORTH, Direction.WEST),
                      "7": (Direction.SOUTH, Direction.WEST), "F": (Direction.SOUTH, Direction.EAST)}

input_array = load_txt_file_as_str(INPUT_FILE_PATH)
print(input_array)
