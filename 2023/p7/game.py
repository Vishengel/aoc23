from hand import Hand, get_card_value

from typing import List, Optional


class HandBid:
    hand: Hand
    bid: int
    rank: Optional[int]
    _value: Optional[int]

    def __init__(self, hand: Hand, bid: int):
        self.hand = hand
        self.bid = bid
        self.rank = None

    @property
    def value(self):
        return self.bid * self.rank


class Game:

    def __init__(self, input_array: List[str]):
        self.hand_bids = [HandBid(Hand(hand_bid.split(" ")[0]), int(hand_bid.split(" ")[1])) for hand_bid in
                          input_array]
        self._sort_hand_bids()
        self._set_ranks()

    def _sort_hand_bids(self):
        self.hand_bids = sorted(self.hand_bids, key=lambda x: str(x.hand.hand_type.value) + x.hand.cards)

    def _set_ranks(self):
        for idx, hand_bid in enumerate(self.hand_bids):
            hand_bid.rank = idx + 1

    def get_winnings(self) -> int:
        return sum([hand_bid.value for hand_bid in self.hand_bids])
