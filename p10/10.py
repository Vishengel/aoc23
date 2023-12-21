from enum import IntEnum
from pathlib import Path
from typing import List, Tuple, Optional

from bidict import bidict

from util import SubProblem, load_txt_file_as_list_of_str, load_txt_file_as_list_of_list_of_str

INPUT_FILE_PATH = Path("input")
SUB_PROBLEM = SubProblem.ONE


class Direction(IntEnum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


SYMBOL_TO_PIPE_MAP = bidict({"|": (Direction.NORTH, Direction.SOUTH), "-": (Direction.EAST, Direction.WEST),
                             "L": (Direction.NORTH, Direction.EAST), "J": (Direction.NORTH, Direction.WEST),
                             "7": (Direction.SOUTH, Direction.WEST), "F": (Direction.EAST, Direction.SOUTH,),
                             ".": (None, None)})

DIR_TO_COORD_CHANGE_MAP = {Direction.NORTH: (-1, 0), Direction.EAST: (0, 1),
                           Direction.SOUTH: (1, 0), Direction.WEST: (0, -1)}


def get_opposite_direction(direction: Direction):
    match direction:
        case Direction.NORTH:
            return Direction.SOUTH
        case Direction.EAST:
            return Direction.WEST
        case Direction.SOUTH:
            return Direction.NORTH
        case Direction.WEST:
            return Direction.EAST


class PipeSegment:
    possible_directions: Tuple[Direction, Direction]
    directions_to_explore: List[Direction]
    coords: Tuple[int, int]
    dist_from_start: int

    def __init__(self, symbol: str, coords: Tuple[int, int], dist_from_start: int,
                 previous_dir: Optional[Direction] = None):
        self.possible_directions = SYMBOL_TO_PIPE_MAP[symbol]
        self.set_directions_to_explore(previous_dir)
        self.coords = coords
        self.dist_from_start = dist_from_start

    def set_directions_to_explore(self, previous_dir: Optional[Direction]):
        if previous_dir is None:
            self.directions_to_explore = list(self.possible_directions)
        else:
            explored_direction = get_opposite_direction(previous_dir)
            self.directions_to_explore = [self.possible_directions[0]
                                          if self.possible_directions[1] == explored_direction
                                          else self.possible_directions[1]]

    def __eq__(self, other):
        assert isinstance(other, PipeSegment)
        return self.coords == other.coords and self.possible_directions == other.possible_directions


class PipeMaze:
    maze_grid: List[List[str]]
    start_coords: Tuple[int, int]  # (y, x)
    pipe: List[PipeSegment]

    def __init__(self, maze_grid: List[List[str]]):
        self.maze_grid = maze_grid
        self.start_coords = self._find_start_coords(self.maze_grid)

        start_symbol = self._find_start_symbol(self.maze_grid, self.start_coords)
        self.pipe = [PipeSegment(start_symbol, self.start_coords, 0)]
        self.maze_grid[self.start_coords[0]][self.start_coords[1]] = start_symbol

    def get_neighboring_pipe_segment(self, from_pipe: PipeSegment, from_direction: Direction) -> PipeSegment:
        new_coords = (from_pipe.coords[0] + DIR_TO_COORD_CHANGE_MAP[from_direction][0],
                      from_pipe.coords[1] + DIR_TO_COORD_CHANGE_MAP[from_direction][1])
        return PipeSegment(self.maze_grid[new_coords[0]][new_coords[1]], new_coords, from_pipe.dist_from_start + 1)

    def explore_pipe(self):
        # Start with the first pipe segment
        queue = [self.pipe[0]]

        while queue:
            current_pipe_segment = queue.pop(0)

            for direction in current_pipe_segment.directions_to_explore:
                next_pipe_segment = self.get_neighboring_pipe_segment(current_pipe_segment, direction)
                if next_pipe_segment not in self.pipe:
                    self.pipe.append(next_pipe_segment)
                    queue.append(next_pipe_segment)

    def find_furthest_distance(self):
        return max(self.pipe, key=lambda pipe_seg: pipe_seg.dist_from_start).dist_from_start

    @staticmethod
    def _find_start_coords(maze_grid: List[List[str]]) -> Tuple[int, int]:
        for y, row in enumerate(maze_grid):
            for x, col in enumerate(row):
                if col == "S":
                    return y, x

        return 0, 0

    @staticmethod
    def _find_start_symbol(maze_grid: List[List[str]], start_coords: Tuple[int, int]) -> str:
        start_y, start_x = start_coords
        possible_dirs = []

        # looking to the north
        if Direction.SOUTH in SYMBOL_TO_PIPE_MAP[maze_grid[start_y - 1][start_x]]:
            possible_dirs.append(Direction.NORTH)

        # looking to the east
        if Direction.WEST in SYMBOL_TO_PIPE_MAP[maze_grid[start_y][start_x + 1]]:
            possible_dirs.append(Direction.EAST)

        # looking to the south
        if Direction.NORTH in SYMBOL_TO_PIPE_MAP[maze_grid[start_y + 1][start_x]]:
            possible_dirs.append(Direction.SOUTH)

        # looking to the west
        if Direction.EAST in SYMBOL_TO_PIPE_MAP[maze_grid[start_y][start_x - 1]]:
            possible_dirs.append(Direction.WEST)

        return SYMBOL_TO_PIPE_MAP.inverse[(possible_dirs[0], possible_dirs[1])]


input_array = load_txt_file_as_list_of_list_of_str(INPUT_FILE_PATH)
pipe_maze = PipeMaze(input_array)
pipe_maze.explore_pipe()
print(pipe_maze.find_furthest_distance())
