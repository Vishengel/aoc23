from collections import Counter
from enum import Enum
from typing import Optional

import config
from util import SubProblem


class HandType(Enum):
    HighCard = 0
    OnePair = 1
    TwoPair = 2
    ThreeOfAKind = 3
    FullHouse = 4
    FourOfAKind = 5
    FiveOfAKind = 6


class Hand:
    cards: str
    hand_type: HandType

    def __init__(self, cards: str):
        self.cards = cards

        self.hand_type = self.get_hand_type(cards)

        if config.SUB_PROBLEM == SubProblem.TWO and "1" in cards:
            if len(cards.replace("1", "")) > 0:
                most_freq_char = find_most_freq_char_in_str(cards.replace("1", ""))
                new_hand_type = self.get_hand_type(cards.replace("1", most_freq_char))

                if new_hand_type.value > self.hand_type.value:
                    self.hand_type = new_hand_type

    @staticmethod
    def get_hand_type(cards: str) -> HandType:
        deduped_cards = list(set(cards))

        if len(deduped_cards) == 1:
            return HandType.FiveOfAKind

        if len(deduped_cards) == 4:
            return HandType.OnePair

        if len(deduped_cards) == 5:
            return HandType.HighCard

        if len(deduped_cards) == 2:
            if cards.count(deduped_cards[0]) == 1 or cards.count(deduped_cards[0]) == 4:
                return HandType.FourOfAKind

            return HandType.FullHouse

        # len(deduped_cards) == 3 at this point
        if any(cards.count(card) == 3 for card in deduped_cards):
            return HandType.ThreeOfAKind

        return HandType.TwoPair


def get_card_value(card: str) -> int:
    if card.isdigit():
        return int(card)

    return config.CARD_MAPPING[card]


def find_most_freq_char_in_str(input_string: str) -> str:
    counter = Counter(input_string)
    res = max(counter, key=counter.get)
    return res
