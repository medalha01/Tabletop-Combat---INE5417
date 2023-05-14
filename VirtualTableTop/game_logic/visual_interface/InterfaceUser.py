# from Board import Board
from VirtualTableTop.game_logic.visual_interface.VirtualTableTopGUI import (
    VirtualTableTopGUI,
)
import json
from py_netgames_client.tkinter_client.PyNetgamesServerListener import (
    PyNetgamesServerListener,
)
from py_netgames_client.tkinter_client.PyNetgamesServerProxy import (
    PyNetgamesServerProxy,
)


class InterfaceUser(PyNetgamesServerListener):
    def __init__(self):
        self.match_id = 0
        self.position = 0
        self.connected = False
        self.gui = VirtualTableTopGUI(self)
        # self.board = Board()
        self.name = ""
        self.start = False
        self.settings = False
        self.master = False
        self.characters = []
        self.has_player_char = False
        self.has_initiave = False

    def set_start(self):
        self.start = True

    def reset(self):
        self.start = False
        self.settings = False
        self.master = False
        self.has_player_char = False
        self.has_initiave = False

    # self.board = Board()

    def save_character(self, filepath):
        with open(filepath) as json_file:
            json_file.write(json.dumps(self.characters))

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

    def send_match(self):
        self.server_proxy.send_match(2)

    def receive_disconnect(self):
        pass

    def receive_error(self, error):
        pass

    def receive_match(self, match):
        print("Match received")
        print("Order", match.position)
        print("Id", match.match_id)

    def receive_move(self, move):
        pass
