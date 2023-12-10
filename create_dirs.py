import os

N_PROBLEMS = 25

def create_skeleton_script(path, idx: int):
    skeleton = """from pathlib import Path
from typing import List

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input")
SUB_PROBLEM = SubProblem.ONE
        """

    with open(os.path.join(path, str(idx) + ".py"), 'w') as skeleton_file:
        skeleton_file.write(skeleton)

def create_input_files(path, idx: int):
    with open(os.path.join(path, "input.txt"), 'w') as _:
        pass

    with open(os.path.join(path, "input_test_" + str(idx) + ".txt"), 'w') as _:
        pass

def prepare_dirs():
    root_path = os.path.dirname(__file__)
    for idx in range(1, N_PROBLEMS+1):
        new_dir_path = os.path.join(root_path, str(idx))
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)
            create_skeleton_script(new_dir_path, idx)
            create_input_files(new_dir_path, idx)


if __name__ == "__main__":
    prepare_dirs()