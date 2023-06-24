

from  VirtualTableTop.game_logic.Action import Action


class Character:
    def __init__(self):
        self.pc : bool
        self.name : str
        self.color : str
        self.position : tuple[int, int]
        self.level : str
        self.hp_max : int
        self.initiative : int
        self.ca : int
        self.speed : float
        self.actions : dict[str : Action]
        self.hp : int
        self.actions_amount : int
        self.moved_amount : float
        self.actions_used : int

    def set_attributes(self, attributes : dict):
        self.pc = attributes["team"]
        self.name = attributes["name"]
        self.color = attributes["color"]
        self.position = attributes["position"]
        self.level = attributes["level"]
        self.hp_max = attributes["hp_max"]
        self.initiative = attributes["initiative"]
        self.ca = attributes["ca"]
        self.speed = attributes["speed"]
        self.hp = self.hp_max
        self.actions_amount = attributes.get("actions_amount", 1)
        self.moved_amount = 0
        self.actions_used = 0
        self.actions = {}
        for action in attributes["actions"]:
            print(action)
            self.list_action(action)

    def set_position(self, position: tuple[int,int]):
        self.position = position

    def list_action(self, action : dict):
        self.actions[action["name"]] = Action()
        self.actions[action["name"]].set_attributes(action)
    
    def get_pc(self):
        return self.pc
    
    def get_name(self):
        return self.name

    def get_action(self, action_name : str):
        return self.actions[action_name]
    
    def get_actions_used(self):
        return self.actions_used

    def get_action_amount(self):
        return self.actions_amount
    
    def get_moved_amount(self):
        return self.moved_amount
    
    def get_position(self):
        return self.position

    def get_speed(self):
        return self.speed
    
    def get_dict(self) -> dict:
        char_dict = {}
        char_dict["pc"] = self.pc
        char_dict["name"] = self.name
        char_dict["color"] = self.color
        char_dict["position"] = self.position
        char_dict["level"] = self.level
        char_dict["hp_max"] = self.hp_max
        char_dict["initiative"] = self.initiative
        char_dict["ca"] = self.ca
        char_dict["speed"] = self.speed
        char_dict["hp"] = self.hp
        char_dict["actions_amount"] = self.actions_amount
        char_dict["moved_amount"] = self.moved_amount
        char_dict["actions_used"] = self.actions_used
        char_dict["actions"] = []
        for action in self.actions.values():
            char_dict["actions"].append(action.get_dict())
        return char_dict

    def increase_actions_used(self):
        self.actions_used += 1
    
    def add_moved_amount(self, dist : float):
        self.moved_amount += dist
    
    def reset_turn_attributes(self):
        self.actions_used = 0
        self.moved_amount = 0
    
    def receive_attack(self, roll : int, dmg : int) -> bool:
        if roll > self.ca:
            print(f"{self.name} hit with {dmg} points of damage")
            self.hp -= dmg
            print(f"HP: {self.hp}")
            if self.hp <= 0:
                print(f"{self.name} died")
                return True
        return False

    def receive_heal(self, heal_amount : int):
        self.hp += heal_amount
        if self.hp > self.hp_max:
            self.hp = self.hp_max

    def is_dead(self) -> bool:
        if self.hp <= 0: 
            return True
        return False

