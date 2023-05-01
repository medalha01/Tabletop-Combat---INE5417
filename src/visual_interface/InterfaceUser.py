from Board import Board
import json


class InterfaceUser:
    def __init__(self, GUI):
        self.match_id = 0
        self.position = 0
        self.connected = False
        self.GUI = GUI
        self.gameboard = Board()
        self.name = ""
        self.start = False
        self.settings = False
        self.master = False
        self.characters = []
        self.has_player_char = False
        self.has_initiave = False

    def set_start(self, matchUUID):
        self.start = True
        self.match_id = matchUUID

    def reset(self):
        self.start = False
        self.settings = False
        self.master = False
        self.has_player_char = False
        self.has_initiave = False
        self.gameboard = Board()

    def save_character(self, filepath):
        with open(filepath) as json_file:
            json_file.write(json.dumps(self.characters))
