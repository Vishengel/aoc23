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
        self.sort_hand_bids()

    def sort_hand_bids(self):
        self.hand_bids = sorted(self.hand_bids, key=lambda x: str(x.hand.hand_type.value) + x.hand.cards)
        print(self.hand_bids)

    def get_strongest_hand(self, hand_list: List[Hand]):
        card_hands = [hand.cards for hand in hand_list]

        for idx in range(len(card_hands[0])):
            cards_at_idx = [get_card_value(card_hand[idx]) for card_hand in card_hands]

            if len(set(cards_at_idx)) == 1:
                continue

    def sort_duplicate_hand_bids(self, hand_bid_list: List[HandBid], sorted_hand_bid_list: List[HandBid]):
        start_idx = end_idx = None

        for idx, hand_bid in enumerate(hand_bid_list):
            # [0, 1, 1, 1, 2, 2, 3]
            if hand_bid_list[idx].hand.hand_type.value == hand_bid_list[idx + 1].hand.hand_type.value:
                if start_idx is None:
                    start_idx = idx
                else:
                    continue
            else:
                if start_idx is None and end_idx is None:
                    sorted_hand_bid_list.append(hand_bid_list[idx])
                    continue
                else:
                    end_idx = idx + 1

                    end_idx = None

    def get_winnings(self) -> int:
        return 0
