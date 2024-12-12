import re
from pathlib import Path
from typing import List, Tuple

from util import SubProblem, load_txt_file_as_str

INPUT_FILE_PATH = Path("input1.txt")
SUB_PROBLEM = SubProblem.TWO

VALID_MUL_REGEX = r"mul\({1}(\d{1,3}),{1}(\d{1,3})\){1}"


def get_digits_from_valid_mul_patterns(instruction_set: str) -> List[str]:
    return re.findall(VALID_MUL_REGEX, instruction_set)


def execute_mul_instruction(instruction: Tuple[str, str]) -> int:
    return int(instruction[0]) * int(instruction[1])


def filter_negated_instructions(instruction_set: str) -> str:
    split_instruction_set = instruction_set.split("don't()")
    filtered_instruction_set = split_instruction_set[0]

    for idx, block in enumerate(split_instruction_set[1:]):
        split_block = block.split("do()")
        if len(split_block) == 1:
            # Block does not contain a do(), so it should not be executed
            continue
        filtered_instruction_set += "".join(split_block[1:])

    return filtered_instruction_set


def main():
    input_string = load_txt_file_as_str(INPUT_FILE_PATH)

    if SUB_PROBLEM == SubProblem.TWO:
        input_string = filter_negated_instructions(input_string)

    valid_mul_patterns = get_digits_from_valid_mul_patterns(input_string)
    print(valid_mul_patterns)
    multiplications = [execute_mul_instruction(instruction) for instruction in valid_mul_patterns]
    result = sum(multiplications)
    print(result)


if __name__ == "__main__":
    main()
