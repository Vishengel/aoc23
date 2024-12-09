import re
from pathlib import Path
from typing import List, Tuple

from util import SubProblem, load_txt_file_as_str

INPUT_FILE_PATH = Path("input1.txt")
SUB_PROBLEM = SubProblem.ONE

VALID_MUL_REGEX = r"mul\({1}(\d{1,3}),{1}(\d{1,3})\){1}"

def get_digits_from_valid_mul_patterns(instruction_set: str) -> List[str]:
    return re.findall(VALID_MUL_REGEX, instruction_set)

def execute_mul_instruction(instruction: Tuple[str, str]) -> int:
    return int(instruction[0]) * int(instruction[1])

def main():
    input_array = load_txt_file_as_str(INPUT_FILE_PATH)
    print(input_array)
    valid_mul_patterns = get_digits_from_valid_mul_patterns(input_array)
    print(valid_mul_patterns)
    multiplications = [execute_mul_instruction(instruction) for instruction in valid_mul_patterns]
    result = sum(multiplications)
    print(result)

if __name__ == "__main__":
    main()
