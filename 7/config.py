from pathlib import Path

from util import SubProblem

INPUT_FILE_PATH = Path("input.txt")
SUB_PROBLEM = SubProblem.TWO

HAND_SIZE = 5

if SUB_PROBLEM == SubProblem.ONE:
    CARD_MAPPING = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14}
else:
    CARD_MAPPING = {"A": 10, "C": 12, "D": 13, "E": 14}
