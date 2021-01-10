from pprint import pprint as pp
from character_tracker.basic_moves import basic_moves
from character_tracker.roller import Roller
from character_tracker.utils import get_int_input, get_str_input


class Character(object):
    """A Monster of the Week game character.

    """

    def __init__(self):
        self.name = None
        self.type = None
        self._charm = 0
        self._cool = 0
        self._sharp = 0
        self._tough = 0
        self._weird = 0
        self.luck = 7
        self.harm = 0
        self.unstable_injury = False
        self.experience = 0
        self.info = None
        self.moves = []
        self.haven = []
        self.gear = []
        self.improvements = []
        self.advanced_improvements = []
        self.history = ""
        self.skills = ["charm", "cool", "sharp", "tough", "weird"]
        self.roller = Roller

    def set_skill_levels(self):
        for skill in self.skills:
            if skill == "charm":
                while True:
                    level = get_int_input(skill + " level?")
                    self.charm = level
                    if self._charm is not None:
                        break
            elif skill == "cool":
                while True:
                    level = get_int_input(skill + " level?")
                    self.cool = level
                    if self.cool is not None:
                        break
            elif skill == "sharp":
                while True:
                    level = get_int_input(skill + " level?")
                    self.sharp = level
                    if self.sharp is not None:
                        break
            elif skill == "tough":
                while True:
                    level = get_int_input(skill + " level?")
                    self.tough = level
                    if self.tough is not None:
                        break
            elif skill == "weird":
                while True:
                    level = get_int_input(skill + " level?")
                    self.weird = level
                    if self.weird is not None:
                        break

    @property
    def charm(self):
        return self._charm

    @charm.setter
    def charm(self, value):
        if self._charm is None and self.charm is None:
            self._charm = 0
        elif self._charm is None and self.charm is not None:
            self._charm = self.charm
        if self._charm + value > 3:
            print(f"You cannot have a Charm value over 3.\n")
            self._charm = None
        elif self._charm + value < -1:
            print(f"You cannot have a Charm value under -1.\n")
            self._charm = None
        else:
            self._charm = value

    @property
    def cool(self):
        return self._cool

    @cool.setter
    def cool(self, value):
        if self._cool is None and self.cool is None:
            self._cool = 0
        elif self._cool is None and self.cool is not None:
            self._cool = self.cool
        if self._cool + value > 3:
            print(f"You cannot have a Cool value over 3.\n")
            self._cool = None
        elif self._cool + value < -1:
            print(f"You cannot have a Cool value under -1.\n")
            self._cool = None
        else:
            self._cool = value

    @property
    def tough(self):
        return self._tough

    @tough.setter
    def tough(self, value):
        if self._tough is None and self.tough is None:
            self._tough = 0
        elif self._tough is None and self.tough is not None:
            self._tough = self.tough
        if self._tough + value > 3:
            print(f"You cannot have a Tough value over 3.\n")
            self._tough = None
        elif self._tough + value < -1:
            print(f"You cannot have a Tough value under -1.\n")
            self._tough = None
        else:
            self._tough = value

    @property
    def weird(self):
        return self._weird

    @weird.setter
    def weird(self, value):
        if self._weird is None and self.weird is None:
            self._weird = 0
        elif self._weird is None and self.weird is not None:
            self._weird = self.weird
        if self._weird + value > 3:
            print(f"You cannot have a Weird value over 3.\n")
            self._weird = None
        elif self._weird + value < -1:
            print(f"You cannot have a Weird value under -1.\n")
            self._weird = None
        else:
            self._weird = value

    @property
    def sharp(self):
        return self._sharp

    @sharp.setter
    def sharp(self, value):
        if self._sharp is None and self.sharp is None:
            self._sharp = 0
        elif self._sharp is None and self.sharp is not None:
            self._sharp = self.sharp
        if self._sharp + value > 3:
            print(f"You cannot have a Sharp value over 3.\n")
            self._sharp = None
        elif self._sharp + value < -1:
            print(f"You cannot have a Sharp value under -1.\n")
            self._sharp = None
        else:
            self._sharp = value

    def act_under_pressure(self):
        move = "act_under_pressure"
        skill = "cool"
        self.print_a_move(move=move, skill=skill, skill_level=self.cool)

    def help_out(self):
        move = "help_out"
        skill = "cool"
        self.print_a_move(move=move, skill=skill, skill_level=self.cool)

    def investigate_a_mystery(self):
        move = "investigate"
        skill = "sharp"
        self.print_a_move(move=move, skill=skill, skill_level=self.sharp)

    def read_a_situation(self):
        move = "read_a_situation"
        skill = "sharp"
        self.print_a_move(move=move, skill=skill, skill_level=self.sharp)

    def kick_some_ass(self):
        move = "kick_some_ass"
        skill = "tough"
        self.print_a_move(move=move, skill=skill, skill_level=self.tough)

    def protect(self):
        move = "protect"
        skill = "tough"
        self.print_a_move(move=move, skill=skill, skill_level=self.tough)

    def manipulate_someone(self):
        move = "manipulate"
        skill = "charm"
        self.print_a_move(move=move, skill=skill, skill_level=self.charm)

    def use_magic(self):
        move = "magic"
        skill = "weird"
        self.print_a_move(move=move, skill=skill, skill_level=self.weird)

    def big_magic(self):
        print(self.get_move_info(None, "big_magic"))
        return self.use_magic()

    def spend_luck(self):
        self.luck -= 1
        print(f"\n{self.info['luck']['1']}")
        if self.luck == 0:
            print(f"\n{basic_moves['luck']['out_of_luck_msg']}")
        return self.get_move_info(None, "luck")

    def do_harm(self):
        print(self.get_move_info(None, "harm"))
        level = get_int_input("harm")
        unstable = get_str_input(", is the wound unstable? y/n")
        if "y" in unstable.lower():
            self.unstable_injury = True
        self.harm += level

    def recovery(self):
        print(self.get_move_info(None, "recovery"))
        level = get_int_input("recovery")
        if self.unstable_injury:
            stable = get_str_input(", has the wound been stabilized? y/n")
            if "y" in stable.lower():
                self.unstable_injury = False
        self.harm -= level

    def character_setup(self):
        self.set_skill_levels()
        self.show_me_the_moves()
        self.make_me_a_haven()
        self.get_me_some_gear()

    def make_a_move(self, move: str, skill: str, skill_level: int) -> (str, str, dict):
        result, roller_output = self.roller(skill, skill_level).main()
        msg_output = self.get_move_info(result, move)
        help_output = self.show_helpful_stuff(move)
        return roller_output, msg_output, help_output

    def get_move_info(self, score: [int, None], move: str):
        if self.unstable_injury:
            self.harm += 1
            print(
                f"Damn this unstable wound! My harm is now {self.harm}!\nAnd it's getting worse!\n"
            )
        if score is None:
            return basic_moves[move]["msg"]
        if score < 7:
            self.experience += 1
            if self.experience >= 5:
                self.level_up()
                self.experience = 0
            return basic_moves[move]["miss_msg"]
        elif 7 <= score < 10:
            return basic_moves[move]["hit_msg"]
        elif 10 <= score < 12:
            return basic_moves[move]["big_hit_msg"]
        elif 12 <= score:
            return basic_moves[move]["adv_hit_msg"]

    def print_a_move(self, move, skill, skill_level):
        roller, msg, help_ = self.make_a_move(
            move=move, skill=skill, skill_level=skill_level
        )
        print()
        print(roller)
        print(msg)
        pp(help_, width=120)
        print()

    def show_helpful_stuff(self, move: str):
        # To be overwritten in child class
        pass

    def show_me_the_moves(self):
        # To be overwritten in child class
        pass

    def make_me_a_haven(self):
        # To be overwritten in child class
        pass

    def get_me_some_gear(self):
        # To be overwritten in child class
        pass

    def remind_me(self):
        # To be overwritten in child class
        pass

    def improve_me(self):
        # TODO: Implement this.
        pass

    def level_up(self):
        # TODO: Implement this.
        pass


if __name__ == "__main__":
    pass
