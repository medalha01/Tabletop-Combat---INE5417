

from Position import Position
from Character import Character
from Queue import Queue
from MatchState import MatchState
from random import randint


class Board:
    def __init__(self) -> None:
        self.positions : list[list[Position]] = []
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

            
