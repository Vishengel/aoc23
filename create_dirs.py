import os

N_PROBLEMS = 25


def create_skeleton_script(path, idx: int):
    skeleton = """from pathlib import Path

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input")
SUB_PROBLEM = SubProblem.ONE

input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
"""

    with open(os.path.join(path, f"p{str(idx)}.py"), 'w') as skeleton_file:
        skeleton_file.write(skeleton)


def create_files(path):
    with open(os.path.join(path, "__init__.py"), 'w') as _:
        pass

    with open(os.path.join(path, "input"), 'w') as _:
        pass

    with open(os.path.join(path, "input_test_1a"), 'w') as _:
        pass


def prepare_dirs():
    root_path = os.path.dirname(__file__)
    for idx in range(1, N_PROBLEMS + 1):
        new_dir_path = os.path.join(root_path, f"p{str(idx)}")
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)
            create_skeleton_script(new_dir_path, idx)
            create_files(new_dir_path)


if __name__ == "__main__":
    prepare_dirs()
