from pathlib import Path
from typing import List

from util import load_txt_file_as_list_of_str

INPUT_FILE_PATH = Path("input")


class Card:
    card_id: int
    winning_numbers: List[int]
    actual_numbers: List[int]
    score: int

    def __init__(self, card_string: str):
        self.init_card(card_string)
        self.get_score()

    def init_card(self, card_string: str):
        header, cards = card_string.split(":")
        winning_numbers_str, actual_numbers_str = cards.split("|")

        self.card_id = int(header.split(" ")[-1])
        self.winning_numbers = [int(number) for number in winning_numbers_str.split(" ") if number.isdigit()]
        self.actual_numbers = [int(number) for number in actual_numbers_str.split(" ") if number.isdigit()]

        assert len(set(self.winning_numbers)) == len(self.winning_numbers), "Duplicate number in set of winning numbers"
        assert len(set(self.actual_numbers)) == len(self.actual_numbers), "Duplicate number in set of actual numbers"

    def get_matches(self):
        matches = []
        actual_numbers_copy = self.actual_numbers.copy()

        for winning_numbers in self.winning_numbers:
            if winning_numbers in actual_numbers_copy:
                matches.append(winning_numbers)
                actual_numbers_copy.remove(winning_numbers)

        return matches

    def get_score(self):
        matches = self.get_matches()

        if len(matches) > 0:
            self.score = 2 ** (len(matches) - 1)
        else:
            self.score = 0

    def get_next_cards(self) -> List[int]:
        matches = self.get_matches()

        return [id for id in range(self.card_id + 1, self.card_id + 1 + len(matches))]


input_array = load_txt_file_as_list_of_str(INPUT_FILE_PATH)

# 4_1
cards_queue = [Card(card_string=card_string) for card_string in input_array]
print(sum([card.score for card in cards_queue]))

# 4_2
cards_dict = {card.card_id: card for card in cards_queue}
card_counts = {card: 0 for card in cards_dict}

for card in cards_queue:
    card_counts[card.card_id] = card_counts[card.card_id] + 1
    next_card_ids = card.get_next_cards()

    for next_card_id in next_card_ids:
        cards_queue.append(cards_dict[next_card_id])

print(sum([card_count for card_count in card_counts.values()]))
