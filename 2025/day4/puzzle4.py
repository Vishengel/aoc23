import copy
from pathlib import Path

from util import SubProblem, load_txt_file_as_list_of_list_of_str

INPUT_FILE_PATH = Path("input1.txt")
SUB_PROBLEM = SubProblem.TWO

ROLL = "@"
EMPTY = "."
AVAILABLE = "x"

def print_grid(grid: list[list[str]]) -> None:
    for row in grid:
        print("".join(row))

def get_directions(x: int, y: int, x_max: int, y_max: int) -> set[tuple[int, int]]:
    possible_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),( 1, -1), (1, 0), (1, 1)]

    return {
        (dx, dy)
        for dx, dy in possible_directions
        if 0 <= x + dx < x_max and 0 <= y + dy < y_max
    }

def find_accessible_rolls(grid: list[list[str]]) -> tuple[int, list[list[str]]]:
    n_accessible_rolls = 0
    marked_grid = [row[:] for row in grid]

    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col != ROLL:
                continue

            adjacent_rolls = 0
            directions = get_directions(x, y, len(row), len(grid))

            if len(directions) < 4:
                n_accessible_rolls += 1
                marked_grid[y][x] = AVAILABLE
                continue

            for (dir_x, dir_y) in directions:
                if grid[y+dir_y][x+dir_x] == ROLL:
                    adjacent_rolls += 1

            if adjacent_rolls < 4:
                n_accessible_rolls += 1
                marked_grid[y][x] = AVAILABLE

    return n_accessible_rolls, marked_grid

def main():
    input_array = load_txt_file_as_list_of_list_of_str(INPUT_FILE_PATH)

    if SUB_PROBLEM == SubProblem.ONE:
        print(find_accessible_rolls(input_array)[0])
        return

    finished = False
    total_accessible_rolls = 0

    while not finished:
        n_accessible_rolls, marked_grid = find_accessible_rolls(input_array)
        total_accessible_rolls += n_accessible_rolls
        finished = (input_array == marked_grid)
        input_array = marked_grid

    print(total_accessible_rolls)


if __name__ == "__main__":
    main()
