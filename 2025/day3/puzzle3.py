from operator import index
from pathlib import Path

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input1.txt")
SUB_PROBLEM = SubProblem.TWO

def find_highest_joltage(bank: str, n_batteries: int) -> int:
    highest_joltage = ""
    remaining_bank = bank
    for idx in range(n_batteries, 0, -1):
        highest_battery = max(remaining_bank) if (idx-1) == 0 else max(remaining_bank[:-(idx-1)])
        highest_joltage += str(highest_battery)
        first_idx = remaining_bank.index(highest_battery)
        remaining_bank = remaining_bank[first_idx+1:]

    return int(highest_joltage)

def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
    n_batteries = 2 if SUB_PROBLEM == SubProblem.ONE else 12
    highest_joltages = [find_highest_joltage(bank, n_batteries) for bank in input_array]
    print(highest_joltages)
    print(sum(highest_joltages))

if __name__ == "__main__":
    main()
