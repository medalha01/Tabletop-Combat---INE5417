

from Character import Character


class Position:
    def __init__(self) -> None:
        self.character : Character = None
    
    def get_position(self):
        self.character

    def set_position(self, char: Character):
        self.character = char
    
    def is_occupied(self) -> bool:
        if self.character != None: return True
        return False

