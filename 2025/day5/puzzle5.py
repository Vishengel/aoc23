from pathlib import Path

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input0.txt")
SUB_PROBLEM = SubProblem.ONE

def sort_ranges(ranges: list[str]) -> list[tuple[int, int]]:
    int_ranges = [(int(range.split("-")[0]), (int(range.split("-")[-1]))) for range in ranges]
    return sorted(int_ranges, key=lambda x: x[0])

def merge_ranges(ranges: list[tuple[int, int]]):
    merged_ranges = []

    for idx, _ in enumerate(ranges):
        if idx == len(ranges) - 1:
            break

        lookahead =  1
        current_range = ranges[idx]
        stop_looping = False
        while not stop_looping:
            if idx + lookahead > len(ranges) - 1:
                break

            if current_range[1] < ranges[idx+lookahead][0]:
                stop_looping = True
            else:
                merged_range = merge_range_pair(ranges[idx], ranges[idx+lookahead])
                current_range = merged_range
                lookahead += 1

        if lookahead > 1:
            del ranges[idx+1:idx+lookahead]
        merged_ranges.append(current_range)

    return merged_ranges

def merge_range_pair(range1: tuple[int, int], range2: tuple[int, int]) -> tuple[int, int]:
    return range1[0], range2[1]

def main():
    input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)
    split_idx = input_array.index("")
    ranges = input_array[:split_idx]
    print(ranges)
    ingredient_ids = input_array[split_idx+1:]

    sorted_ranges = sort_ranges(ranges)
    print(sorted_ranges)

    merged_ranges = merge_ranges(sorted_ranges)
    print(merged_ranges)
    print(ingredient_ids)

if __name__ == "__main__":
    main()
