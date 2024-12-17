from pathlib import Path
from typing import List, Dict, Optional

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input1.txt")
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

    def handle_updates(self) -> int:
        update_counter = 0
        for update in self.updates:
            if SUB_PROBLEM == SubProblem.ONE and self._is_correct_update(update):
                update_counter += self._get_middle_page_number(update)
            elif SUB_PROBLEM == SubProblem.ONE and not self._is_correct_update(update):
                update_counter += self._get_middle_page_number(update, True)

        return update_counter

    def _is_correct_update(self, update: List[int]) -> bool:
        for idx, page_number in enumerate(update):
            if page_number not in self.rules:
                # In this case, there are no rules that state that dictate that some numbers can't follow this number
                continue
            rules_for_page_number = set(self.rules[page_number])
            rest_of_update = set(update[:idx])

            if len(rules_for_page_number.intersection(rest_of_update)) > 0:
                return False

        return True

    def _get_middle_page_number(self, update: List[int], fix_ordering: bool = False) -> int:
        assert len(update) % 2 == 1, f"Length of update is {update} is even"

        if fix_ordering:
            update = self._fix_ordering(update)

        return update[len(update) // 2]

    def _fix_ordering(self, update: List[int]) -> List[int]:
        # Placeholder for problem b
        return update


def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
    update_handler = UpdateHandler(input_array=input_array)
    page_number_sum = update_handler.handle_updates()
    print(page_number_sum)


if __name__ == "__main__":
    main()
