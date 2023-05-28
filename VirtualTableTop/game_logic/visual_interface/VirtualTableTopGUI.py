import tkinter as tk
from tkinter import *
import random
import os
from tkinter import messagebox
from tkinter import font
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
            command=self.interface.send_match,
        )
        matchMenu.add_command(
            label="Configure Match",
            command=lambda: self.notify_message("Something went wrong!"),
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
        textboxes_window = tk.Toplevel()
        textboxes_window.title("Character Creation")
        textboxes_window.geometry("300x300")
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

            # Store the textbox entry in the dictionary with the label as the key
            self.textbox_entries[status[i]] = textbox

        # Create a button to retrieve the values
        button_frame = tk.Frame(textboxes_window, bg="#3B3B3B", padx=5, pady=5)
        button_frame.pack(side="top", fill="x")
        retrieve_button = tk.Button(
            button_frame,
            text="Retrieve Values",
            command=lambda: self.retrieve_values(textboxes_window),
        )
        retrieve_button.pack(side="bottom", pady=10)

        button_frame = tk.Frame(textboxes_window, bg="#3B3B3B", padx=5, pady=5)
        button_frame.pack(side="bottom", fill="both", expand=True)

    def retrieve_values(self, window):
        # Retrieve the values from the textbox entries
        for label, entry in self.textbox_entries.items():
            value = entry.get()
            print(f"{label}: {value}")

        # Close the window after retrieving values
        window.destroy()
