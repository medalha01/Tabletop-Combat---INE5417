

from  VirtualTableTop.game_logic.Character import Character


class Position:
    def __init__(self) -> None:
        self.character : Character = None
    
    def get_position(self) -> Character:
        return self.character

    def set_position(self, char: Character):
        self.character = char
    
    def is_occupied(self) -> bool:
        if self.character != None: return True
        return False

