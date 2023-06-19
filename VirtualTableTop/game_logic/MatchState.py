

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
                char = position.get_position()
                name = '' if char == None else char.name
                aux.append(name)
            self.positions.append(aux)
    
    def set_characters(self, characters):
        for character in characters.values():
            char_dict = character.get_dict()
            self.characters[char_dict["name"]] = char_dict
    
    def set_character(self, character):
        if character != None:
            self.character = character.get_dict()
    
    def set_initiative_queue(self, queue):
        for char in queue:
            self.initiative_queue.append(char.name)


