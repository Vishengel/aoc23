from pathlib import Path

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input3.txt")
SUB_PROBLEM = SubProblem.TWO


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

def get_similarity_score(list0, list1) -> int:
    transposition_table = {}
    similarity_score = 0

    for digit0 in list0:
        if digit0 in transposition_table:
            similarity_score += transposition_table[digit0]
            continue

        count = 0
        for digit1 in list1:
            if digit1 == digit0:
                count += 1

        score = digit0*count
        transposition_table[digit0] = score
        similarity_score += score

    return similarity_score


def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
    list0, list1 = split_list_and_sort(input_array)
    if SUB_PROBLEM == SubProblem.ONE:
        total_distance = get_dist(list0, list1)
        print(total_distance)
    else:
        similarity_score = get_similarity_score(list0, list1)
        print(similarity_score)

if __name__ == "__main__":
    main()
