from character_tracker.character import Character
from character_tracker.utils import validate_option_choice, get_int_input
from pprint import pprint as pp


class Professional(Character):
    def __init__(self):
        super().__init__()

    def show_me_the_moves(self):
        limit = int(self.info["moves"]["limit"])
        pp(self.info["moves"], width=120)
        print(
            f"Chose {limit} expert moves.\nEnter the number associated with each chosen move separately."
        )
        valid_choices = [
            int(choice)
            for choice in list(self.info["moves"].keys())
            if choice != "limit"
        ]
        for _ in range(limit):
            while True:
                choice = get_int_input("what move you'd like to chose")
                if not validate_option_choice(
                    choice=choice, valid_choices=valid_choices, chosen=self.moves
                ):
                    break

    def get_me_some_gear(self):
        def gear_chooser(title, category):
            limit = int(category["limit"])
            pp(category, width=120)
            print(
                f"Chose {limit} {title}.\nEnter the number associated with each chosen {title} separately."
            )
            valid_choices = [
                int(choice) for choice in list(category.keys()) if choice != "limit"
            ]
            for _ in range(limit):
                while True:
                    choice = get_int_input(f"what {title} you'd like to chose")
                    if not validate_option_choice(
                        choice=choice, valid_choices=valid_choices, chosen=self.gear
                    ):
                        break

        if isinstance(self.info["gear"], dict):
            for title_, category_ in self.info["gear"].items():
                gear_chooser(title_, category_)
        else:
            gear_chooser("weapon", self.info["gear"])

    def remind_me(self) -> None:
        output = {
            "moves": {},
            "gear": {},
        }
        for move in self.moves:
            name, _, description = self.info["moves"][str(move)].partition(":")
            output["moves"][name] = description
        for item in self.gear:
            for category, gear in self.info["gear"].items():
                if str(item) in gear:
                    name, _, description = self.info["gear"][category][
                        str(item)
                    ].partition(":")
                    output["gear"][name] = description
        pp(output)
        pp(
            {
                key: val
                for key, val in self.__dict__.items()
                if isinstance(val, int) or isinstance(val, str)
            },
            depth=1,
        )

    def show_helpful_stuff(self, move: str) -> dict:
        output = {}
        move_keys = [int(key) for key in self.info["keys"]["moves"][move]]
        for move_key in move_keys:
            if move_key in self.moves:
                title, _, description = self.info["moves"][str(move_key)].partition(":")
                output[title] = description
        if not output:
            output = (
                "You don't have any Expert moves or Haven options to help with this."
            )
        return output
