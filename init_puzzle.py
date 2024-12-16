import pathlib
from pathlib import Path

YEAR = 2024
DAY = 5


def create_dir() -> Path:
    root_dir = pathlib.Path(__file__).parent.resolve()
    year_dir = root_dir / str(YEAR)
    puzzle_dir = year_dir / f"day{DAY}"
    puzzle_dir.mkdir(parents=True, exist_ok=True)
    return puzzle_dir


def create_skeleton_script(puzzle_dir):
    skeleton = """from pathlib import Path

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input0.txt")
SUB_PROBLEM = SubProblem.ONE

def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)

if __name__ == "__main__":
    main()
"""
    path = (puzzle_dir / f"puzzle{DAY}.py")

    if path.exists():
        print(f"File puzzle{DAY}.py already exists in {puzzle_dir}")
        return

    with open(path, 'w') as skeleton_file:
        skeleton_file.write(skeleton)


def create_files(puzzle_dir: Path):
    create_skeleton_script(puzzle_dir)
    for idx in range(4):
        try:
            (puzzle_dir / f"input{idx}.txt").touch(exist_ok=False)
        except FileExistsError:
            print(f"File input{idx}.txt already exists in {puzzle_dir}")
            continue


def main():
    puzzle_dir = create_dir()
    create_files(puzzle_dir)


if __name__ == "__main__":
    main()
