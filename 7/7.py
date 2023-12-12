from pathlib import Path

from game import Game
from util import load_txt_file_as_list_of_str, SubProblem

INPUT_FILE_PATH = Path("input_test_7.txt")
SUB_PROBLEM = SubProblem.ONE

# hand1 = Hand("AAAAA")
# hand2 = Hand("AA8AA")
# hand3 = Hand("23332")
# hand4 = Hand("TTT98")
# hand5 = Hand("23432")
# hand6 = Hand("A23A4")
# hand7 = Hand("23456")

def replace_non_digit_cards_in_str(cards: str) -> str:
    return cards.replace("A", "E").replace("T", "A").replace("J", "B").replace("Q", "C").replace("K", "D")

input_array = [replace_non_digit_cards_in_str(cards) for cards in load_txt_file_as_list_of_str(INPUT_FILE_PATH)]
game = Game(input_array)
print(game.get_winnings())