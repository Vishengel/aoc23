from pathlib import Path
from typing import List

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input")
SUB_PROBLEM = SubProblem.TWO


class Race:
    time: int
    dist_record: int
    winning_times: List[int]

    def __init__(self, time: int, distance: int):
        self.time = time
        self.dist_record = distance
        self.winning_times = []
        self.get_winning_times()

    def get_winning_times(self):
        for button_press_time in range(1, self.time):
            duration = self.time - button_press_time
            dist = duration * button_press_time

            if dist > self.dist_record:
                self.winning_times.append(button_press_time)

            if len(self.winning_times) > 0 and dist <= self.dist_record:
                return


input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)

if SUB_PROBLEM == SubProblem.ONE:
    times = [int(time) for time in input_array[0].split(":")[1].split(" ") if time.isdigit()]
    dist_records = [int(dist_record) for dist_record in input_array[1].split(":")[1].split(" ") if dist_record.isdigit()]
else:
    times = [int(time) for time in input_array[0].split(":")[1].replace(" ", "").split(" ") if time.isdigit()]
    dist_records = [int(dist_record) for dist_record in input_array[1].replace(" ", "").split(":")[1].split(" ") if
                    dist_record.isdigit()]

races = [Race(time, dist_record) for time, dist_record in zip(times, dist_records)]

margin_of_error = 1
for race in races:
    margin_of_error *= len(race.winning_times)

print(margin_of_error)
