import re
from pathlib import Path
from typing import List, Tuple

from util import SubProblem, load_txt_file_as_str

INPUT_FILE_PATH = Path("input1.txt")
SUB_PROBLEM = SubProblem.TWO

VALID_MUL_REGEX = r"mul\({1}(\d{1,3}),{1}(\d{1,3})\){1}"
DO_REGEX = r'\bdo\b(?!n\'t)'
DONT_DO_LAZY_REGEX = r"(don't\(\).*)(?:do\(\)+?)"

def get_digits_from_valid_mul_patterns(instruction_set: str) -> List[str]:
    return re.findall(VALID_MUL_REGEX, instruction_set)


def execute_mul_instruction(instruction: Tuple[str, str]) -> int:
    return int(instruction[0]) * int(instruction[1])


def filter_disables(instruction_set: str, enable: bool = True) -> str:
    split_token = "don't()" if enable else "do()"
    split_instruction_set = instruction_set.split(split_token) # if enable else re.split(DO_REGEX, instruction_set)

    if len(split_instruction_set) == 1 and enable:
        return ""

    enable_blocks = split_instruction_set[0::2] if enable else split_instruction_set[1::2]
    disable_blocks = split_instruction_set[1::2] if enable else split_instruction_set[0::2]

    for block in disable_blocks:
        filtered_string = filter_disables(block, not enable)
        enable_blocks.append(filtered_string)

    return "".join(enable_blocks)


def main():
    input_string = load_txt_file_as_str(INPUT_FILE_PATH)
    print(input_string)

    if SUB_PROBLEM == SubProblem.TWO:
        # input_string = filter_disables(input_string)
        input_string = re.sub(DONT_DO_LAZY_REGEX, "do()", input_string)
        print(input_string)

    valid_mul_patterns = get_digits_from_valid_mul_patterns(input_string)
    print(valid_mul_patterns)
    multiplications = [execute_mul_instruction(instruction) for instruction in valid_mul_patterns]
    result = sum(multiplications)
    print(result)


if __name__ == "__main__":
    main()
