from pathlib import Path

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input0.txt")
SUB_PROBLEM = SubProblem.ONE

def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)

if __name__ == "__main__":
    main()
