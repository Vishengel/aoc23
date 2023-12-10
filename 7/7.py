from enum import Enum
from pathlib import Path
from typing import List

from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input")
SUB_PROBLEM = SubProblem.ONE

CARD_MAPPING = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

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

    return CARD_MAPPING[card]

hand1 = Hand("AAAAA")
hand2 = Hand("AA8AA")
hand3 = Hand("23332")
hand4 = Hand("TTT98")
hand5 = Hand("23432")
hand6 = Hand("A23A4")
hand7 = Hand("23456")
