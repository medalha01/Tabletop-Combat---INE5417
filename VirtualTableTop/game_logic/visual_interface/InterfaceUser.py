# from Board import Board
from VirtualTableTop.game_logic.visual_interface.VirtualTableTopGUI import (
    VirtualTableTopGUI,
)
from VirtualTableTop.game_logic.Board import (
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
import os


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
        self.add_listener()

    def set_start(self):
        self.start = True

    def reset(self):
        self.start = False
        self.settings = False
        self.master = False
        self.has_player_char = False
        self.has_initiave = False
        self.board = Board()
        self.local_characters = []
        self.gui.update_context_button(0)
    
    def set_initiative(self):
        self.has_initiave = True

    def save_character(self):

        for char in self.local_characters:
            filepath = '{}.json'.format(char.get_name())
            with open(filepath) as json_file:
                json_file.write(json.dumps(char.get_dict()))


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
        print(action_name, act_pos)
        my_turn = self.board.is_my_turn(self.local_characters)
        if my_turn:
            notification = self.board.use_action(action_name, act_pos)
            if notification["message"] == "":
                self.server_proxy.send_move(self.match_id, notification["payload"])
                self.update_view()
            else:
                self.gui.notify_message(notification["message"])
        self.check_game_over()
    
    def skip_turn(self):
        my_turn = self.board.is_my_turn(self.local_characters)
        if my_turn and self.has_initiave:
            self.board.set_next_turn()
            payload = {
                "message_type": "skip_turn", 
                "content": True
            }
            self.server_proxy.send_move(self.match_id, payload)
            self.update_view()

    def check_game_over(self):
        if self.board.game_over:
            answer = messagebox.askquestion('Game Over', 'Do you want to save your character?', icon='warning')
            if answer == 'yes':
                self.save_character('')
            self.server_proxy.send_disconnect()

    def update_view(self):
        match_state = self.board.get_match_state()
        match_status = sum([self.settings, self.has_initiave])+1 if self.master else 3
        self.gui.update_view(match_status, match_state)
    
    def make_character(self, char_info):
        if not(self.start or self.has_player_char) and self.settings:
            print(f"creating char:\n{char_info}")
            if not self.master:
                self.has_player_char = True
                char_info["team"] = True
            else:
                char_info["team"] = False
            
            self.create_character(char_info, True)
            self.send_character(char_info)
            self.update_view()
        else:
            if not self.settings:
                messagebox.showinfo('Action not permitted', 'Match not configured', icon='warning')
            if self.start:
                messagebox.showinfo('Action not permitted', 'Combat already started', icon='warning')
            else:
                messagebox.showinfo('Action not permitted', 'Players can only have one character', icon='warning')

    def send_character(self, char_info: dict):
        payload = {
            "message_type" : "character",
            "content" : char_info
        }
        self.server_proxy.send_move(self.match_id, payload)

    def send_match_settings(self, settings):
        if self.master:
            self.board.update_position_matrix(settings["board_size"], settings["board_size"])
            self.gui.update_board_image(settings["filename"])
            self.gui.update_board({}, settings["board_size"]*[settings["board_size"]*['']])
            payload = {
                "message_type" : "settings",
                "content" : settings
            }
            self.server_proxy.send_move(self.match_id, payload)
            self.settings = True
            self.gui.update_context_button(2)
        else:
            messagebox.showinfo('Action not permitted', 'Only the master can configure the match', icon='warning')

    def send_iniciative(self):
        amount_of_pcs = self.board.get_character_count() - len(self.local_characters)
        print(amount_of_pcs, (self.master and self.settings and (amount_of_pcs == self.number_of_players-1)))
        if self.master and self.settings and (amount_of_pcs == self.number_of_players-1):
            self.set_start()
            payload = {
                "message_type" : "start",
                "content" : True
            }
            self.server_proxy.send_move(self.match_id, payload)

            payload = self.board.calculate_initiative()
            print(payload)
            self.set_initiative()
            self.server_proxy.send_move(self.match_id, payload)
            self.update_view()

    def create_character(self, char_info: dict, my_char: bool):
        char = self.board.create_character(char_info)
        if my_char:
            self.add_as_controllable_character(char)
        
    def start_match(self, is_master: bool, number_of_players: int):
        self.master = is_master
        self.number_of_players = number_of_players
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
        if answer == 'yes':
            self.send_connect()
        else:
            self.gui.destroy()
            exit()

    def receive_error(self, error):
        self.reset()
        answer = messagebox.askquestion('Disconnection Error', 'Do you want to reconnect?', icon='warning')
        if answer == 'yes':
            self.send_connect()
        else:
            self.gui.destroy()
            exit()

    def receive_match(self, match):
        self.match_id = match.match_id
        self.position = match.position
        print("Match received")
        print("Order", match.position)
        print("Id", match.match_id)
        if self.master:
            self.gui.update_context_button(1)
            self.gui.open_settings_window()
        else:
            self.gui.update_context_button(3)

    def receive_move(self, move):
        message = move.payload["message_type"]
        content = move.payload["content"]
        if message == 'settings':
            self.settings = True
            self.board.update_position_matrix(content["board_size"], content["board_size"])
            self.gui.update_board_image(content["filename"])
            self.gui.update_board({}, content["board_size"]*[content["board_size"]*['']])
        elif message == 'character':
            self.create_character(content, False)
        elif message == 'start':
            self.set_start()
        elif message == 'initiative':
            self.board.set_initiative_queue(content)
            self.set_initiative()
        elif message == 'move_char':
            self.board.move_character(*content)
        elif message == 'attack':
            self.board.receive_attack(*content)
            self.check_game_over()
        elif message == 'heal':
            self.board.receive_heal(*content)
        elif message == 'skip_turn':
            self.board.set_next_turn()
        
        self.update_view()

