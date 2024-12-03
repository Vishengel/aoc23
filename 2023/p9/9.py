from pathlib import Path
from typing import List

from p9.p9_util import int_list_from_str
from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input")
SUB_PROBLEM = SubProblem.TWO


def get_next_seq(old_seq: List[int]) -> List[int]:
    return [old_seq[idx] - old_seq[idx - 1] for idx, number in enumerate(old_seq[1:], start=1)]


def get_next_value_in_history(seq: List[int]) -> int:
    if all([number == 0 for number in seq]):
        return 0

    return seq[-1] + get_next_value_in_history(get_next_seq(seq))


def get_first_value_in_history(seq: List[int]) -> int:
    if all([number == 0 for number in seq]):
        return 0

    return seq[0] - get_first_value_in_history(get_next_seq(seq))


input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
input_seqs = [int_list_from_str(line) for line in input_array]

if SUB_PROBLEM == SubProblem.ONE:
    print(sum([get_next_value_in_history(input_seq) for input_seq in input_seqs]))
else:
    print(sum([get_first_value_in_history(input_seq) for input_seq in input_seqs]))
