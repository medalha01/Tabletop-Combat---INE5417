

from random import randint


class Action:
    def __init__(self) -> None:
        self.name : str
        self.type : str
        self.dices :list[int]
        self.roll_bonus : int
        self.dmg_bonus : int
        self.range : float
        self.aoe_radius : int
        self.max_amount : int
        self.times_used : int

    def get_max_amount(self) -> int:
        return self.max_amount
    
    def get_times_used(self) -> int:
        return self.times_used
    
    def get_range(self) -> float:
        return self.range
    
    def get_aoe(self) -> int:
        return self.aoe_radius
    
    def get_type(self) -> str:
        return self.type
    
    def get_dict(self) -> dict:
        action_dict = {}
        action_dict["name"] = self.name
        action_dict["type"] = self.type
        action_dict["dices"] = self.dices
        action_dict["roll_bonus"] = self.roll_bonus
        action_dict["dmg_bonus"] = self.dmg_bonus
        action_dict["range"] = self.range
        action_dict["aoe_radius"] = self.aoe_radius
        action_dict["max_amount"] = self.max_amount
        action_dict["times_used"] = self.times_used

        return action_dict
    
    def increase_times_used(self):
        self.times_used += 1
    
    def set_attributes(self, attributes : dict):    
        self.name = attributes["name"]
        self.type = attributes["type"]
        self.dices = attributes["dices"]
        self.roll_bonus = attributes["roll_bonus"]
        self.dmg_bonus = attributes["dmg_bonus"]
        self.range = attributes["range"]
        self.aoe_radius = attributes["aoe_radius"]
        self.max_amount = attributes["max_amount"]
        self.times_used = 0
    
    def calculate_effect(self) -> int:
        x_numbers = []
        for dice in self.dices:
            x_numbers.append(randint(1, dice))
        amount = sum(x_numbers) + self.dmg_bonus
        return amount

    def calculate_roll(self) -> int:
        return (randint(1,20) + self.roll_bonus)
