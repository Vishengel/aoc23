from math import gcd
from pathlib import Path
from typing import List

from p8.p8_util import get_node_list
from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input")
SUB_PROBLEM = SubProblem.TWO


def find_n_steps_subproblem_one(nodes, instructions) -> int:
    n_steps = 0
    current_node = "AAA"
    while current_node != "ZZZ":
        for idx, instruction in enumerate(instructions):
            if instruction == "L":
                current_node = nodes[current_node][0]
            else:
                current_node = nodes[current_node][1]

            n_steps += 1

            if current_node == "ZZZ" or idx == (len(instructions) - 1):
                break

    return n_steps


def all_nodes_end_in_z(nodes: List[str]):
    return all(node[-1] == "Z" for node in nodes)


def lcm(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)


def find_lcm_of_list(numbers: List[int]) -> int:
    result_lcm = numbers[0]
    for i in range(1, len(numbers)):
        result_lcm = lcm(result_lcm, numbers[i])
    return result_lcm


def find_n_steps_subproblem_two(nodes, instructions) -> int:
    starting_nodes = []
    for node in nodes.keys():
        if node[-1] == "A":
            starting_nodes.append(node)

    n_cycle_steps_list = []
    for starting_node in starting_nodes:
        current_nodes = [starting_node]
        n_cycle_steps = 0

        while not all_nodes_end_in_z(current_nodes):
            for instruction_idx, instruction in enumerate(instructions):
                for node_idx, current_node in enumerate(current_nodes):
                    if instruction == "L":
                        current_nodes[node_idx] = nodes[current_node][0]
                    else:
                        current_nodes[node_idx] = nodes[current_node][1]

                n_cycle_steps += 1

                if all_nodes_end_in_z(current_nodes) or instruction_idx == (len(instructions) - 1):
                    break

        n_cycle_steps_list.append(n_cycle_steps)

    return find_lcm_of_list(n_cycle_steps_list)


input_array = [line for line in load_txt_file_as_list_of_str(INPUT_FILE_PATH) if len(line) > 0]
instructions = input_array[0]
nodes = get_node_list(input_array)

if SUB_PROBLEM == SubProblem.ONE:
    n_steps = find_n_steps_subproblem_one(nodes, instructions)
    print(n_steps)
else:
    n_steps = find_n_steps_subproblem_two(nodes, instructions)
    print(n_steps)
