

from Position import Position
from Character import Character
from Queue import Queue
from MatchState import MatchState
from random import randint


class Board:
    def __init__(self) -> None:
        self.positions : list[list[Position]]
        self.characters : dict[str : Character] = []
        self.initiative_queue : Queue = Queue()
        self.game_over : bool = False
    
    def get_match_state(self) -> MatchState:
        match_state = MatchState()
        match_state.set_position(self.positions)
        match_state.set_characters(self.characters)
        match_state.set_character(self.initiative_queue.top())
        match_state.set_initiative_queue(self.initiative_queue.queue())
        return match_state
    
    def is_my_turn(self, user_chars) -> bool:
        for char in user_chars:
            if char == self.initiative_queue.top():
                return True
        return False
    
    def check_for_gameover(self):
        pc, npc, dead_pc, alve_pc = 0, 0, 0, 0
        for char in self.characters:
            if char.get_pc: 
                pc+=1
                if char.is_dead(): dead_pc +=1
            else: 
                npc+=1
                if char.is_dead(): dead_npc +=1
        if (npc == dead_npc) or (pc == dead_pc):
            return True
        return False
    
    def update_position_matrix(self, lentgh : int, height : int):
        self.positions = height * [lentgh * [Position()]]
    
    def set_initiative_queue(self, initiative_queue: list[str]):
        for char in initiative_queue:
            self.initiative_queue.push(self.characters[char])
    
    def set_next_turn(self):
        current_char = self.initiative_queue.pop()
        current_char.reset_turn_attributes()
        self.initiative_queue.push(current_char)
    
    def add_character(self, char: Character):
        self.characters[char.name] = char
    
    def create_character(self, char_info: dict) -> Character:
        char = Character()
        char.set_attributes(char_info)
        self.add_character(char)
        return char

    def calculate_initiative(self):
        initiative_list = []
        for char in self.characters:
            x = randint(1,20)
            x += char.initiative
            initiative_list.append((x, char.name))
        
        initiative_list.sort()
        for char in initiative_list:
            self.initiative_queue.push(self.characters[char[1]])
        
        payload = {
            "message_type" : "initiative",
            "content" : initiative_list
        }
        
        return payload
    
    def calculate_distance(self, start_pos: tuple[int, int], end_pos: tuple[int, int]) -> float:
        x0, y0 = start_pos
        x, y = end_pos
        dx = abs(x-x0)
        dy = abs(y-y0)
        dmax = max(dx, dy)
        dist = dmax*1.5
        return dist

    def calculate_affected_characters(self, attack_pos : tuple[int, int], action) -> list[Character]:
        affected_characters = []
        for char in self.characters:
            char_pos = char.get_position()
            char_dist = self.calculate_distance(attack_pos, char_pos)
            if char_dist <= action.get_aoe():
                affected_characters.append(char)
        return affected_characters

    def move_character(self, position: tuple[int, int], dist : float):
        char = self.initiative_queue.top()
        init_pos = char.get_position()
        init_pos = self.positions[init_pos[0]][init_pos[1]]
        init_pos.set_position(None)
        new_pos = self.positions[position[0]][position[1]]
        new_pos.set_position(char)
        char.add_moved_amount(dist)
        char.set_position(position)

    def use_move(self, pos_cord: tuple[int, int]) -> dict:
        notification = {}
        position = self.positions[pos_cord[0]][pos_cord[1]]
        occupied = position.is_occupied()
        if not occupied:
            current_char = self.initiative_queue.top()
            init_pos = current_char.get_position()
            mov_amount = current_char.get_moved_amount()
            speed = current_char.get_speed()
            dist = self.calculate_distance(init_pos, pos_cord)
            notification["dist"] = dist
            if (mov_amount + dist) <= speed:
                self.move_character(pos_cord, dist)
                notification["message"] = ""
            else:
                notification["message"] = "Position too far from character"
        else:
            notification["message"] = "Position already occupied"

        return notification

    def receive_attack(self, roll : int, damage: int, action_name: str, affected_characters: list[str]):
        character = self.initiative_queue.top()
        character.increase_actions_used()
        action = character.get_actions(action_name)
        action.increase_times_used()

        for name in affected_characters:
            character = self.characters[name]
            dead = character.receive_attack(roll, damage)
            if dead:
                pos = character.get_position()
                self.positions[pos[0]][pos[1]].set_position(None)
                self.initiative_queue.remove(character)
        
        self.game_over = self.check_for_gameover()

    def receive_heal(self, roll: int, heal_amount: int, action_name: str, affected_characters: list[str]):
        character = self.initiative_queue.top()
        character.increase_actions_used()
        action = character.get_actions(action_name)
        action.increase_times_used()

        for name in affected_characters:
            character = self.characters[name]
            character.receive_heal(roll, heal_amount)

    def make_attack(self, action_name: str, position: tuple[int,int]) -> dict:
        character = self.initiative_queue.top()
        action = character.get_action(action_name)
        affected_characters = self.calculate_affected_characters(position, action)
        roll = action.calculate_roll()
        dmg = action.calculate_effect()

        self.receive_attack(roll, dmg, action_name, affected_characters)

        payload = {
            "message_type" : "attack",
            "content": [roll, dmg, affected_characters]
        }
        return payload

    def make_heal(self, action_name: str, position: tuple[int,int]) -> dict:
        character = self.initiative_queue.top()
        action = character.get_action(action_name)
        affected_characters = self.calculate_affected_characters(position, action)
        roll = action.calculate_roll()
        heal = action.calculate_effect()

        self.receive_heal(roll, heal, action_name, affected_characters)

        payload = {
            "message_type" : "heal",
            "content": [roll, heal, affected_characters]
        }
        return payload

    def use_action(self, action_name: str, act_pos: tuple[int, int]) -> dict:
        character:Character = self.initiative_queue.top()
        act_used = character.get_actions_used()
        act_amount = character.get_action_amount()
        payload = ""

        if act_used < act_amount:
            action = character.get_action(action_name)
            max_amount = action.get_max_amount()
            times_used = action.get_times_used()

            if times_used < max_amount:
                char_pos = character.get_position()
                act_range = action.get_range()
                dist = self.calculate_distance(act_pos, char_pos)
                
                if dist <= act_range:
                    act_type = action.get_type()

                    if act_type == "attack":
                        payload = self.make_attack(action_name, act_pos)
                    elif act_type == "heal":
                        payload = self.make_heal(action_name, act_pos)
        return payload

