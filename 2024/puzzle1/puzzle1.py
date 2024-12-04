from pathlib import Path

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input1.txt")
SUB_PROBLEM = SubProblem.ONE


def split_list_and_sort(input_array):
    list0 = []
    list1 = []
    for line in input_array:
        digits = line.split("  ")
        list0.append(int(digits[0]))
        list1.append(int(digits[1]))
    return sorted(list0), sorted(list1)


def get_dist(list0, list1) -> int:
    total_distance = 0
    for (digit0, digit1) in zip(list0, list1):
        total_distance += abs(digit0 - digit1)
    return total_distance

def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
    # print(input_array)
    list0, list1 = split_list_and_sort(input_array)
    # print(list0)
    # print(list1)
    total_distance = get_dist(list0, list1)
    print(total_distance)


if __name__ == "__main__":
    main()
