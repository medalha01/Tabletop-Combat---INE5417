import tkinter as tk
from tkinter import *
import random
import os
from tkinter import messagebox
from tkinter import font
from VirtualTableTop.game_logic.visual_interface.CharacterSidebar import CharacterSidebar
from VirtualTableTop.game_logic.visual_interface.InitiativeSidebar import InitiativeSidebar
from PIL import Image, ImageTk
from VirtualTableTop.game_logic.visual_interface.windows import CreateCharWindow, SettingWindow, StartMatchWindow
from VirtualTableTop.game_logic.MatchState import MatchState

class VirtualTableTopGUI(tk.Tk):
    def __init__(self, interface):
        super().__init__()
        self._action_selected = ""
        self.interface = interface

        self.title("Virtual Table Top")
        self.geometry("1280x720")
        self.setMenu()
        self.setBar()
        # VirtualTableTop/game_logic/visual_interface/
        # self.setCanvas(
        #     os.path.join(os.path.dirname(__file__), "../assets/asset.jpg"), 32
        # )
        self.update_board_image(os.path.join(os.path.dirname(__file__), "../assets/asset.jpg"))
        self.update_board({}, [['','','','1',''],['2','','','3',''],['','','3','',''], ['','','3','',''], ['','','3','','']])
        self.textbox_entries = {}
        self.isWindowOpen = False

    def setCanvas(self, backgroundImageName, tileSize):
        self.tile_size = tileSize
        self.grid_width = 100  # image.width // self.tile_size
        self.grid_height = 100  # image.height // self.tile_size
        image = Image.open(backgroundImageName)
        image = image.resize((tileSize, tileSize), Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(image)
        self.img = background_image
        self.canvas = tk.Canvas(
            self,
            bg="#F7F7F7",  # width=800, height=600,
            scrollregion=(
                0,
                0,
                tileSize * self.grid_width + 20,
                tileSize * self.grid_height + 20,
            ),
        )
        self.canvas.pack(side="right", fill="both", expand=True)

        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        self.tiles = []
        for row in range(self.grid_height):
            tile_row = []
            for col in range(self.grid_width):
                x1 = col * self.tile_size
                y1 = row * self.tile_size
                x2 = x1 + self.tile_size
                y2 = y1 + self.tile_size
                self.canvas.create_image(x1, y1, anchor="nw", image=self.img)
                tile = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="", outline="black"
                )
                tile_row.append(tile)
            self.tiles.append(tile_row)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self._y_canvas_scrollbar = tk.Scrollbar(self.canvas)
        self._y_canvas_scrollbar.pack(side="right", fill="y")
        self._y_canvas_scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self._y_canvas_scrollbar.set)
        self._x_canvas_scrollbar = tk.Scrollbar(self.canvas, orient="horizontal")
        self._x_canvas_scrollbar.pack(side="bottom", fill="x")
        self._x_canvas_scrollbar.config(command=self.canvas.xview)
        self.canvas.config(xscrollcommand=self._x_canvas_scrollbar.set)

    def update_board_image(self, file_name):
        self.image_file_name = file_name

    def update_view(self, match_status: int, match_state: MatchState):

        self.update_board(match_state.characters, match_state.postions)

        self.update_initiative(match_state.characters, match_state.initiative_queue)

        self.update_character(match_state.character)

        self.update_context_button(match_status)

    def update_board(self, characters: dict[str : dict], postions: list[list[str]]):

        self.grid_width = len(postions[0])
        self.grid_height = len(postions)

        self.tile_size = int(600//(max(self.grid_width, self.grid_height)))
        image = Image.open(self.image_file_name)
        image = image.resize((self.tile_size, self.tile_size), Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(image)
        self.img = background_image
        self.canvas = tk.Canvas(
            self,
            bg="#3B3B3B", #width=800, height=600,
            scrollregion=(
                0,
                0,
                self.tile_size * self.grid_width + 20,
                self.tile_size * self.grid_height + 20,
            ),
        )
        self.canvas.pack(side="right", fill="both", expand=True)

        self.tiles = []
        for row in range(self.grid_height):
            tile_row = []
            for col in range(self.grid_width):
                x1 = col * self.tile_size
                y1 = row * self.tile_size
                x2 = x1 + self.tile_size
                y2 = y1 + self.tile_size
                self.canvas.create_image(x1, y1, anchor="nw", image=self.img)
                tile = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="", outline="black"
                )
                if postions[row][col] != '':
                    color = f"#{random.randint(0, 0xFFFFFF):06x}"
                    self.canvas.itemconfig(tile, fill=color)
                tile_row.append(tile)
            self.tiles.append(tile_row)
        # self.canvas.bind("<Button-1>", self.on_canvas_click)

        self._y_canvas_scrollbar = tk.Scrollbar(self.canvas)
        self._y_canvas_scrollbar.pack(side="right", fill="y")
        self._y_canvas_scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self._y_canvas_scrollbar.set)
        self._x_canvas_scrollbar = tk.Scrollbar(self.canvas, orient="horizontal")
        self._x_canvas_scrollbar.pack(side="bottom", fill="x")
        self._x_canvas_scrollbar.config(command=self.canvas.xview)
        self.canvas.config(xscrollcommand=self._x_canvas_scrollbar.set)

    def update_initiative(self, characters: dict[str : dict], initiative_queue: list[str]):
        self._sidebar_init.update_char_info(characters, initiative_queue)

    def update_character(self, character: dict):
        self._sidebar_char.update_char_info(character)
        self._sidebar_char.update_action_list(character["actions"])

    def update_context_button(self, ):
        pass

    def on_canvas_click(self, event):
        col = int((event.x) // self.tile_size)
        row = int((event.y) // self.tile_size)
        tile = self.tiles[row][col]
        color = f"#{random.randint(0, 0xFFFFFF):06x}"
        if self.canvas.itemcget(tile, "fill") == "":
            self.canvas.itemconfig(tile, fill=color)
        else:
            self.canvas.itemconfig(tile, fill="")

    def setMenu(self):
        appMenubar = Menu(self)

        self.config(menu=appMenubar)

        file_menu = Menu(appMenubar)
        matchMenu = Menu(appMenubar)
        characterMenu = Menu(appMenubar)
        notifyMenu = Menu(appMenubar)

        file_menu.add_command(
            label="Connect",
            command=self.interface.add_listener,
        )
        file_menu.add_command(
            label="Disconnect",
            command=lambda: self.notify_message("Something went wrong!"),
        )

        matchMenu.add_command(
            label="Start Match",
            command=self.interface.start_match,
        )
        matchMenu.add_command(
            label="Configure Match",
            command=lambda: self.interface.send_match_settings,
        )

        characterMenu.add_command(label="Make Character", command=self.interface.make_character)
        characterMenu.add_command(
            label="Save Character",
            command=lambda: self.notify_message("Something went wrong!"),
        )
        characterMenu.add_command(
            label="Load Character",
            command=lambda: self.notify_message("Something went wrong!"),
        )

        notifyMenu.add_command(
            label="Error", command=lambda: self.notify_message("Something went wrong!")
        )

        appMenubar.add_cascade(label="Conectar", menu=file_menu)
        appMenubar.add_cascade(label="Match", menu=matchMenu)
        appMenubar.add_cascade(label="Personagem", menu=characterMenu)
        appMenubar.add_cascade(label="Notificar", menu=notifyMenu)

    def setBar(self):
        self._sidebar_char = CharacterSidebar(self)
        self.update_character({"name":"arindel",'level':'10', 'hp':'100', 'hp_max':'120', 'initiative':'3','ca':'14','moved_amount':'3','speed':'6',
                               'actions': [{'name':'sword slash', 'dices':(2, 4)},{'name':'heal', 'dices':(1, 4)}]})

        # sidebar_char = tk.Frame(self, bg="#3B3B3B", width=200)
        self._sidebar_char.frame.pack(side="left", fill="y")

        self._sidebar_init = InitiativeSidebar(self)
        self.update_initiative({'troy':{'name':'troy', 'level':'10', 'hp':'100', 'hp_max':'120', 'initiative':'3'}}, ['troy']*2)

        self._sidebar_init.frame.pack(side="right", fill="both")

    def notify_message(self, mensagem):
        messagebox.showinfo("Warning", mensagem)

    def open_char_creation(self):
        CCW = CreateCharWindow()
        CCW.open_window()
        CCW.set_interface(self.interface)

    def open_start_match(self):
        SMW = StartMatchWindow()
        SMW.open_window()
        SMW.set_interface(self.interface)

    def open_settings_window(self):
        SW = SettingWindow()
        SW.open_window()
        SW.set_interface(self.interface)
        # self.update_board_image()
        # self.update_board()

    def select_action(self, action_name=''):
        self._action_selected = action_name
        print(f"acao {self._action_selected} selecionada")