import math
import re
from enum import Enum
from pathlib import Path
from typing import Dict

from util import load_txt_file_as_list_of_str


class CubeColor(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Game:
    GAME_REGEX = r"game (\d+)"
    COLOR_REGEX = r"(\d+) {color}"

    game_id: int
    max_n_cubes: Dict[CubeColor, int]
    power: int

    def __init__(self, game_string: str):
        self.game_id = 0
        self.max_n_cubes = {CubeColor.RED: 0, CubeColor.GREEN: 0, CubeColor.BLUE: 0}

        self.parse_game_string(game_string)
        self.get_power()

    def parse_game_string(self, game_string: str):
        game_string = game_string.lower()
        self.game_id = int(re.findall(self.GAME_REGEX, game_string)[0])

        for color in CubeColor:
            color_counts = re.findall(self.COLOR_REGEX.format(color=color.value), game_string)
            self.max_n_cubes[color] = max([int(color_count) for color_count in color_counts])

    def get_power(self):
        self.power = math.prod(self.max_n_cubes.values())

    def is_possible(self, cube_limits: Dict[CubeColor, int]) -> bool:
        return all(self.max_n_cubes[color] <= cube_limits[color] for color in CubeColor)

    def __repr__(self):
        return f"Game {self.game_id}: {self.max_n_cubes[CubeColor.RED]} red - {self.max_n_cubes[CubeColor.GREEN]} green - " \
               f"{self.max_n_cubes[CubeColor.BLUE]} blue max_n_cubes: {self.max_n_cubes} - power {self.power}"


CUBE_LIMITS = {CubeColor.RED: 12, CubeColor.GREEN: 13, CubeColor.BLUE: 14}
INPUT_FILE_PATH = Path("input")

game_strings_list = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
game_list = [Game(game_string) for game_string in game_strings_list]

id_sum = sum(game.game_id for game in game_list if game.is_possible(CUBE_LIMITS))
print(id_sum)

power_sum = sum(game.power for game in game_list)
print(power_sum)
