from pathlib import Path
from typing import List, Dict, Optional

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input0.txt")
SUB_PROBLEM = SubProblem.ONE


class UpdateHandler:
    RULE_SEPARATOR = "|"
    UPDATE_SEPARATOR = ","
    rules: Dict[int, List[int]] = {}
    updates: List[List[int]] = []

    def __init__(self, input_array: List[str]):
        self._parse_input(input_array)
        print(self.rules)
        print(self.updates)

    def _parse_input(self, input_array: List[str]):
        breakline = self._parse_rules(input_array)
        assert breakline is not None and breakline < (len(input_array) - 1)

        self._parse_updates(input_array[breakline + 1:])

    def _parse_rules(self, input_array: List[str]) -> Optional[int]:
        for idx, line in enumerate(input_array):
            if line == "":
                return idx
            self._parse_rule(line)
        # There is no empty line in the input
        return None

    def _parse_rule(self, line: str):
        first_page_number, second_page_number = (int(page_number) for page_number in line.split(self.RULE_SEPARATOR))

        if first_page_number in self.rules:
            self.rules[first_page_number].append(second_page_number)
        else:
            self.rules[first_page_number] = [second_page_number]

    def _parse_updates(self, updates: List[str]):
        for line in updates:
            self._parse_update(line)

    def _parse_update(self, line: str):
        update_list = [int(page_number) for page_number in line.split(self.UPDATE_SEPARATOR)]
        self.updates.append(update_list)


def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
    update_handler = UpdateHandler(input_array=input_array)


if __name__ == "__main__":
    main()
