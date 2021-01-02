import pickle
from pprint import pprint as pp
from pkg_resources import resource_stream, resource_exists, resource_filename
from sys import exit
from .utils import get_int_input


class Tracker(object):
    """Tracker for multiple Monster of the Week game characters.

    Saves and loads characters in pickle format.
    """

    def __init__(self):
        self.characters = {}
        try:
            self.character_file = resource_stream(__name__, "pickle/characters.pkl")
        except FileNotFoundError:
            self.character_file = None
        self.character_file_name = resource_filename(
            __name__, "pickle/characters.pkl"
        )
        if resource_exists(__name__, "pickle/characters.pkl"):
            self.load_characters()

    def chose_character(self):
        char_cd = {i: name for i, name in enumerate(list(self.characters.keys()), 1)}
        print()
        print("Your characters:")
        pp(char_cd)
        while True:
            choice = get_int_input("character choice")
            if choice in list(char_cd.keys()):
                return self.characters[char_cd[choice]]
            else:
                print(f'"{choice}" is not a valid choice.')

    def save_characters(self):
        with open(self.character_file_name, "wb") as f:
            pickle.dump(self.characters, f)

    def load_characters(self):
        if not self.character_file:
            return
        try:
            self.characters = pickle.load(self.character_file)
            return 1
        except FileNotFoundError:
            print("You haven't created any characters yet.")

    def quit(self):
        self.save_characters()
        exit()


if __name__ == "__main__":
    pass
