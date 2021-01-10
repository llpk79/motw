from pprint import pprint as pp
from character_tracker.character import Character
from character_tracker.utils import validate_option_choice, get_int_input


class Initiate(Character):
    def __init__(self):
        super().__init__()

    def get_me_some_gear(self):
        pass

    def show_me_the_moves(self):
        pass

    def make_me_a_haven(self):
        pass

    def remind_me(self):
        pass

    def show_helpful_stuff(self, move: str):
        pass
