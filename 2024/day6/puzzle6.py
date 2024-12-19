from pathlib import Path
from typing import List, Tuple, Set

from util import SubProblem, load_txt_file_as_list_of_list_of_str, is_out_of_bounds

INPUT_FILE_PATH = Path("input1.txt")
SUB_PROBLEM = SubProblem.ONE


class PatrolMap:
    EMPTY_SYMBOL = "."
    OBSTACLE_SYMBOL = "#"
    VISITED_SYMBOL = "X"
    DIRECTION_SUCCESSOR = {"^": ">", ">": "v", "v": "<", "<": "^"}
    DIRECTION_INCREMENTS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

    def __init__(self, map_array: List[List[str]]):
        self.patrol_map = map_array
        self.x_pos, self.y_pos, self.direction = self._find_start_position_and_direction(map_array)
        self.visited_positions: Set[Tuple[int, int]] = {(self.x_pos, self.y_pos)}
        self.guard_has_left = False

    def _find_start_position_and_direction(self, map_array: List[List[str]]):
        for y, row in enumerate(map_array):
            for x, col in enumerate(row):
                if col in self.DIRECTION_SUCCESSOR:
                    return x, y, col

    def traverse_map(self):
        while not self.guard_has_left:
            self._move()

    def _move(self):
        direction_increment = self.DIRECTION_INCREMENTS[self.direction]
        new_x = self.x_pos + direction_increment[0]
        new_y = self.y_pos + direction_increment[1]

        if is_out_of_bounds(self.patrol_map, new_x, new_y):
            self.guard_has_left = True
            return

        if self._is_obstacle(new_x, new_y):
            self._change_direction()
            return

        self.patrol_map[self.y_pos][self.x_pos] = self.EMPTY_SYMBOL
        self.x_pos = new_x
        self.y_pos = new_y

        self.patrol_map[new_y][new_x] = self.direction
        self.visited_positions.add((new_x, new_y))

    def _change_direction(self):
        new_direction = self.DIRECTION_SUCCESSOR[self.direction]
        self.patrol_map[self.y_pos][self.x_pos] = new_direction
        self.direction = new_direction

    def _is_obstacle(self, x_pos: int, y_pos: int) -> bool:
        return self.patrol_map[y_pos][x_pos] == self.OBSTACLE_SYMBOL

    def __repr__(self):
        map_string = ""
        for row in self.patrol_map:
            map_string += "".join(row) + "\n"
        return map_string

    def print_map_with_visited_locations(self):
        new_map = self.patrol_map.copy()
        for (x, y) in self.visited_positions:
            new_map[y][x] = self.VISITED_SYMBOL
        for row in new_map:
            print("".join(row))


def main():
    input_array = load_txt_file_as_list_of_list_of_str(INPUT_FILE_PATH)
    patrol_map = PatrolMap(input_array)
    print(patrol_map)
    patrol_map.print_map_with_visited_locations()
    patrol_map.traverse_map()
    patrol_map.print_map_with_visited_locations()
    print(len(patrol_map.visited_positions))


if __name__ == "__main__":
    main()
