from pathlib import Path
from typing import Dict, Optional, List, Tuple

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input1.txt")
SUB_PROBLEM = SubProblem.TWO

transposition_table: Dict[str, bool] = {}


def is_acceptable_level_difference(digit0: int, digit1: int) -> bool:
    return 1 <= abs(digit0 - digit1) <= 3


def is_ascending(digit0: int, digit1: int) -> bool:
    return digit0 < digit1


def report_is_safe(report: str) -> bool:
    digits = [int(digit) for digit in report.split(" ")]

    if report in transposition_table:
        return transposition_table[report]

    if not is_acceptable_level_difference(digits[0], digits[1]):
        transposition_table[report] = False
        return False

    ascending = is_ascending(digits[0], digits[1])

    for idx in range(1, len(digits) - 1):
        if not is_acceptable_level_difference(digits[idx], digits[idx + 1]) or ascending != is_ascending(digits[idx],
                                                                                                         digits[
                                                                                                             idx + 1]):
            transposition_table[report] = False
            return False

    transposition_table[report] = True
    return True

class Report:
    report_string: str
    digits: Tuple[int]
    unsafe_level_removed: bool
    ascending: bool

    def __init__(self, report_string: Optional[str] = None, digits: Optional[List[int]] = None, unsafe_level_removed: bool = False, ascending: Optional[bool] = None):
        assert (report_string is not None or digits is not None)
        if report_string is not None:
            self.report_string = report_string
            self.digits = tuple([int(digit) for digit in report_string.split()])
        elif digits is not None:
            self.digits = tuple(digits)
            self.report_string = " ".join(map(str, digits))

        self.unsafe_level_removed = unsafe_level_removed
        self.ascending = ascending

    def get_report_with_digit_removed(self, idx: int) -> "Report":
        if idx == 0:
            return Report(digits=self.digits[1:], unsafe_level_removed=True, ascending=None)

        return Report(digits=self.digits[:idx] + self.digits[idx+1:], unsafe_level_removed=True, ascending=None)


    def __hash__(self):
        return hash((self.report_string, self.digits, self.unsafe_level_removed))

    def __repr__(self):
        return f"{self.report_string}[{self.unsafe_level_removed}]"


def report_is_safe_with_dampener(report: Report, depth: int = 0) -> bool:
    if report in transposition_table:
        return transposition_table[report]

    if report.ascending is None:
        report.ascending = is_ascending(report.digits[0], report.digits[1])

    for idx in range(0, len(report.digits) - 1):
        if not is_acceptable_level_difference(report.digits[idx], report.digits[idx + 1]):
            if report.unsafe_level_removed:
                transposition_table[report] = False
                return False
            is_safe = report_is_safe_with_dampener(report=report.get_report_with_digit_removed(idx), depth=depth + 1) or \
                report_is_safe_with_dampener(report=report.get_report_with_digit_removed(idx+1), depth=depth + 1)
            transposition_table[report] = is_safe
            return is_safe
        if report.ascending != is_ascending(report.digits[idx], report.digits[idx + 1]):
            if report.unsafe_level_removed:
                transposition_table[report] = False
                return False

            if idx == 1:
                is_safe = report_is_safe_with_dampener(report=report.get_report_with_digit_removed(idx), depth=depth + 1) or \
                    report_is_safe_with_dampener(report=report.get_report_with_digit_removed(idx+1), depth=depth + 1) or \
                report_is_safe_with_dampener(report=report.get_report_with_digit_removed(idx - 1), depth=depth + 1)
                transposition_table[report] = is_safe
                return is_safe

            is_safe = report_is_safe_with_dampener(report=report.get_report_with_digit_removed(idx), depth=depth + 1) or \
                report_is_safe_with_dampener(report=report.get_report_with_digit_removed(idx+1), depth=depth + 1)
            transposition_table[report] = is_safe
            return is_safe

    transposition_table[report] = True
    return True


def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
    n_safe = 0
    for report in input_array:
        n_safe += report_is_safe(report) if SubProblem == SUB_PROBLEM.ONE else report_is_safe_with_dampener(Report(report))
    print(n_safe)
    for k, v in transposition_table.items():
        print(f"{k} --- {v}")


if __name__ == "__main__":
    main()
