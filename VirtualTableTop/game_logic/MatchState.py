

class MatchState:
    def __init__(self) -> None:
        self.positions : list[list[str]] = []
        self.characters : dict[str : dict] = {}
        self.initiative_queue : list[str] = []
        self.character : dict = {}
        self.game_over : bool
    
    def set_position(self, positions):
        for line in positions:
            aux = []
            for position in line:
                aux.append(position.get_position().name)
            self.positions.append(aux)
    
    def set_characters(self, characters):
        for character in characters:
            char_dict = character.get_dict()
            self.characters[char_dict["name"]] = char_dict
    
    def set_character(self, character):
        self.character = character.get_dict()
    
    def set_initiative_queue(self, queue):
        for char in queue:
            self.initiative_queue.append(char.name)


