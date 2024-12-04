import os
import pathlib
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

YEAR = 2024
DAY = 1
SESSION_COOKIE = os.getenv("AOC_SESSION")


def create_dir() -> Path:
    root_dir = pathlib.Path(__file__).parent.resolve()
    year_dir = root_dir / str(YEAR)
    puzzle_dir = year_dir / f"puzzle{DAY}"
    puzzle_dir.mkdir(parents=True, exist_ok=True)
    return puzzle_dir


def create_skeleton_script(path):
    skeleton = """from pathlib import Path

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input")
SUB_PROBLEM = SubProblem.ONE

input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
"""

    with open(os.path.join(path, f"puzzle{DAY}.py"), 'w') as skeleton_file:
        skeleton_file.write(skeleton)


def get_input():
    input_url = f"https://adventofcode.com/{YEAR}/day/{DAY}/input"


def create_files(puzzle_dir: Path):
    create_skeleton_script(puzzle_dir)


def main():
    puzzle_dir = create_dir()
    create_files(puzzle_dir)


if __name__ == "__main__":
    main()
