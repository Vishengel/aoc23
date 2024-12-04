from typing import List, Dict, Tuple


def get_node_list(input_array: List[str]) -> Dict[str, Tuple[str, str]]:
    nodes = {}

    for _, node_string in enumerate(input_array[1:]):
        node_string_cleaned = node_string.replace("(", "").replace(")", "").replace(",", "")
        node_split = node_string_cleaned.split(" ")
        nodes[node_split[0]] = (node_split[2], node_split[3])

    return nodes
