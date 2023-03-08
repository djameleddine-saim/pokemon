from pokemon import *

class Attaque:
    def __init__(self, name: str, lower: int, upper: int, target_other: bool, cost: int):
        self.name = name
        self.lower = lower
        self.upper = upper
        self.target_other = target_other
        self.cost = cost

    def get_value_random(self):
        return random.randint(self.lower, self.upper)