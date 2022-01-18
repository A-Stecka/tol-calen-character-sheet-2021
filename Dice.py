import random
import json


class Dice:

    def __init__(self, no_of_sides):
        self.__no_of_sides = no_of_sides

    def roll(self):
        return random.randint(1, self.__no_of_sides)

    def roll_for(self, attribute_val, skill_val):
        result = random.randint(1, self.__no_of_sides)
        if result == self.__no_of_sides:
            return False
        if result == 1 or result <= attribute_val + skill_val:
            return True
        return False

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
