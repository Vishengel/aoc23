from pathlib import Path
from typing import List, Optional

from util import load_txt_file_as_list_of_str

INPUT_FILE_PATH = Path("input")


def is_symbol(char: str) -> Optional[str]:
    if (not char.isdigit()) and (char != "."):
        return char

    return None


def is_adjacent_to_symbol(input_array: List[str], y: int, x: int) -> Optional[str]:
    coords = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)]

    for coord in coords:
        try:
            if symbol := is_symbol(input_array[y + coord[0]][x + coord[1]]):
                return symbol, y + coord[0], x + coord[1]
        except IndexError:
            continue

    return None, None, None


input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
valid_numbers = []
number_string = ""
number_is_adjacent_to_symbol = False

for y, row in enumerate(input_array):
    if number_is_adjacent_to_symbol:
        valid_numbers.append((int(number_string), symbol_coords[0], symbol_coords[1], symbol_coords[2]))
        symbol_coords = (None, None, None)

    number_string = ""
    number_is_adjacent_to_symbol = False

    for x, col in enumerate(row):
        if col.isdigit():
            number_string += col
            if is_adjacent_to_symbol(input_array, y, x) != (None, None, None):
                symbol_coords = is_adjacent_to_symbol(input_array, y, x)
                number_is_adjacent_to_symbol = True
        else:
            if number_is_adjacent_to_symbol:
                valid_numbers.append((int(number_string), symbol_coords[0], symbol_coords[1], symbol_coords[2]))
                symbol_coords = (None, None, None)

            number_string = ""
            number_is_adjacent_to_symbol = False

print(sum([number[0] for number in valid_numbers]))

potential_gears = [number for number in valid_numbers if number[1] == "*"]
gear_ratios = []

for idx, number in enumerate(potential_gears):
    for idx2, number2 in enumerate(potential_gears[idx+1:]):
        if number[2] == number2[2] and number[3] == number2[3]:
            gear_ratios.append(number[0] * number2[0])

print(sum(gear_ratios))