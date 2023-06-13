# from Board import Board
from VirtualTableTop.game_logic.visual_interface.VirtualTableTopGUI import (
    VirtualTableTopGUI,
)
from VirtualTableTop.game_logic.visual_interface.Board import (
    Board,
)
import json
from py_netgames_client.tkinter_client.PyNetgamesServerListener import (
    PyNetgamesServerListener,
)
from py_netgames_client.tkinter_client.PyNetgamesServerProxy import (
    PyNetgamesServerProxy,
)
from tkinter import messagebox


class InterfaceUser(PyNetgamesServerListener):
    def __init__(self):
        self.match_id = 0
        self.position = 0
        self.number_of_players = 0
        self.gui = VirtualTableTopGUI(self)
        self.board = Board()
        self.name = ""
        self.start = False
        self.settings = False
        self.master = False
        self.local_characters = []
        self.has_player_char = False
        self.has_initiave = False
        self.connected = False

    def set_start(self):
        self.start = True

    def reset(self):
        self.start = False
        self.settings = False
        self.master = False
        self.has_player_char = False
        self.has_initiave = False
        self.board = Board()
    
    def set_initiative(self):
        self.has_initiave = True

    def save_character(self, filepath):
        with open(filepath) as json_file:
            json_file.write(json.dumps(self.local_characters))

    def add_as_controllable_character(self, character):
        self.local_characters.append(character)
    
    def position_click(self, position: tuple[int,int]):
        my_turn = self.board.is_my_turn(self.local_characters)
        if my_turn:
            notification = self.board.use_move(position)
            if notification["message"] == "":
                self.server_proxy.send_move(self.match_id, notification["payload"])
                self.update_view()
            else:
                self.gui.notify_message(notification["message"])
    
    def action_click(self, action_name: str, act_pos: tuple[int,int]):
        print(action_name)
        my_turn = self.board.is_my_turn(self.local_characters)
        if my_turn:
            notification = self.board.use_action(action_name, act_pos)
            if notification["message"] == "":
                self.server_proxy.send_move(self.match_id, notification["payload"])
                self.update_view()
            else:
                self.gui.notify_message(notification["message"])
    
    def skip_turn(self):
        self.board.set_next_turn()
        payload = {
            "message_type": "skip_turn", 
            "content": True
        }
        self.server_proxy.send_move(self.match_id, payload)
        self.update_view()

    def update_view(self):
        match_state = self.board.get_match_state()
        match_status = sum([self.start, self.settings, self.has_player_char, self.has_initiave])
        self.gui.update_view(match_status, match_state)
    
    def make_character(self):
        if not(self.start or self.has_player_char):
            char_info = self.gui.open_char_creation()
        
        if not self.master:
            self.has_player_char = True
            char_info["team"] = "pc"
        else:
            char_info["team"] = "npc"
        
        self.create_character(char_info, True)
        self.send_character(char_info)
    
    def send_character(self, char_info: dict):
        payload = {
            "message_type" : "character",
            "content" : char_info
        }
        self.server_proxy.send_move(self.match_id, payload)

    def send_match_settings(self):
        settings = self.gui.open_settings_window()
        self.board.update_position_matrix()
        payload = {
            "message_type" : "settings",
            "content" : settings
        }
        self.server_proxy.send_move(self.match_id, payload)

    def send_iniciative(self):
        amount_of_pcs = self.board.get_character_count() - len(self.local_characters)
        if self.master and self.settings and (amount_of_pcs == self.number_of_players):
            self.set_start()
            payload = {
                "message_type" : "start",
                "content" : True
            }
            self.server_proxy.send_move(self.match_id, payload)

            payload = self.board.calculate_initiative()
            self.set_initiative()
            self.server_proxy.send_move(self.match_id, payload)

    def create_character(self, char_info: dict, my_char: bool):
        char = self.board.create_character(char_info)
        if my_char:
            self.add_as_controllable_character(char)
        
    def start_match(self):
        is_master, number_of_players = self.gui.open_start_match()
        if is_master:
            self.master = True

        self.server_proxy.send_match(number_of_players)

    def disconnect(self):
        self.server_proxy.send_disconnect()

    def main(self):
        self.gui.mainloop()

    def add_listener(self):
        self.server_proxy = PyNetgamesServerProxy()
        self.server_proxy.add_listener(self)
        self.send_connect()

    def send_connect(self):
        self.server_proxy.send_connect("wss://py-netgames-server.fly.dev/")

    def receive_connection_success(self):
        print("Connection Success")
        self.connected = True

    def send_match(self, amount_of_players: int):
        self.server_proxy.send_match(amount_of_players)

    def receive_disconnect(self):
        self.reset()
        answer = messagebox.askquestion('Disconnection From Server', 'Do you want to reconnect?', icon='warning')
        if answer:
            self.server_proxy.send_connect()
        else:
            exit()

    def receive_error(self, error):
        self.reset()
        answer = messagebox.askquestion('Disconnection Error', 'Do you want to reconnect?', icon='warning')
        if answer:
            self.server_proxy.send_connect()
        else:
            exit()

    def receive_match(self, match):
        self.match_id = match.match_id
        self.position = match.position
        print("Match received")
        print("Order", match.position)
        print("Id", match.match_id)

    def receive_move(self, move):
        pass
