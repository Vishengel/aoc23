from pathlib import Path

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input")
SUB_PROBLEM = SubProblem.ONE

input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
