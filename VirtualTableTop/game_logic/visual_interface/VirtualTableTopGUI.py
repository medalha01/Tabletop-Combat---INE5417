import tkinter as tk
from tkinter import *
import random
import os
from tkinter import messagebox
from VirtualTableTop.game_logic.visual_interface.CharacterSidebar import (
    CharacterSidebar,
)
from VirtualTableTop.game_logic.visual_interface.InitiativeSidebar import (
    InitiativeSidebar,
)
from PIL import Image, ImageTk


class VirtualTableTopGUI(tk.Tk):
    def __init__(self, interface):
        super().__init__()

        self.interface = interface

        self.title("Virtual Table Top")
        self.geometry("800x600")
        self.setMenu()
        self.setBar()
        # VirtualTableTop/game_logic/visual_interface/
        self.setCanvas(
            os.path.join(os.path.dirname(__file__), "../assets/asset.jpg"), 32
        )

    def setCanvas(self, backgroundImageName, tileSize):
        self.canvas = tk.Canvas(self, bg="#F7F7F7", width=800, height=600)
        self.canvas.pack(side="right", fill="both", expand=True)
        self.tile_size = tileSize
        image = Image.open(backgroundImageName)
        background_image = ImageTk.PhotoImage(image)
        self.img = background_image
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)

        self.grid_width = self.img.width() // self.tile_size
        self.grid_height = self.img.height() // self.tile_size

        self.tiles = []
        for row in range(self.grid_height):
            tile_row = []
            for col in range(self.grid_width):
                x1 = col * self.tile_size
                y1 = row * self.tile_size
                x2 = x1 + self.tile_size
                y2 = y1 + self.tile_size
                tile = self.canvas.create_rectangle(x1, y1, x2, y2, fill="", outline="")
                tile_row.append(tile)
            self.tiles.append(tile_row)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def on_canvas_click(self, event):
        col = event.x // self.tile_size
        row = event.y // self.tile_size
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
            command=lambda: self.notify_message("Something went wrong!"),
        )
        matchMenu.add_command(
            label="Configure Match",
            command=self.interface.send_match,
        )

        characterMenu.add_command(
            label="Make Character", command=self.open_textboxes_window
        )
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

        # sidebar_char = tk.Frame(self, bg="#3B3B3B", width=200)
        self._sidebar_char.frame.pack(side="left", fill="y")

        self._sidebar_init = InitiativeSidebar(self)
        self._sidebar_init.frame.pack(side="right", fill="y")

    def notify_message(self, mensagem):
        messagebox.showinfo("Warning", mensagem)

    def open_textboxes_window(self):
        textboxes_window = Toplevel()
        textboxes_window.title("Character Creation")
        textboxes_window.geometry("300x200")
        status = ["Name", "Level", "HP", "Initiative", "CA", "Speed"]
        for i in range(6):
            label_frame = tk.Frame(textboxes_window, bg="#3B3B3B", padx=5, pady=5)
            label_frame.pack(side="top", fill="x")

            textbox_label = tk.Label(
                label_frame,
                text=status[i],
                font=("helvetica", 12),
                bg="#3B3B3B",
                fg="#e3e3e3",
                width=10,
            )
            textbox_label.pack(side="left")

            textbox = tk.Entry(label_frame)
            textbox.pack(side="right", expand=True, fill="x", padx=5)
