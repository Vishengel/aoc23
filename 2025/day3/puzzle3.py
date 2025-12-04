from pathlib import Path

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input0.txt")
SUB_PROBLEM = SubProblem.ONE

def find_highest_joltage(bank: str):
    highest_joltage = 0
    for idx, battery in enumerate(bank[:-1]):
        highest_next = max([int(next_bat) for next_bat in bank[idx+1:]])
        joltage = int(battery + str(highest_next))
        highest_joltage = joltage if joltage > highest_joltage else highest_joltage
    return highest_joltage

def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
    highest_joltages = [find_highest_joltage(bank) for bank in input_array]
    print(highest_joltages)
    print(sum(highest_joltages))

if __name__ == "__main__":
    main()
