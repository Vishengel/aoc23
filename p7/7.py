import config
from game import Game
from util import load_txt_file_as_list_of_str


def replace_non_digit_cards_in_str(cards: str) -> str:
    return cards.replace("A", "E").replace("T", "A").replace("J", "1").replace("Q", "C").replace("K", "D")


input_array = [replace_non_digit_cards_in_str(cards) for cards in load_txt_file_as_list_of_str(config.INPUT_FILE_PATH)]
game = Game(input_array)
print(game.get_winnings())

# 22333
# 22334
## B2334 => 32334