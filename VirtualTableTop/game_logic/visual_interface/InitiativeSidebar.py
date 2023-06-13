from VirtualTableTop.game_logic.visual_interface.Widget import Widget
import tkinter as tk
from tkinter import font


class InitiativeSidebar(Widget):
    def __init__(self, window) -> None:
        super().__init__(window)

        # Character Info

        self._initiave_text = tk.Label(
            self.frame,
            text="Initiative",
            bg="#3B3B3B",
            font=("helvetica", 30),
            fg="#e3e3e3",
            padx=10,
        )
        self._initiave_text.pack(side="top")

        self._character_listbox = tk.Listbox(
            self.frame,
            bg="#3B3B3B",
            font=("helvetica", 16),
            fg="#e3e3e3",
            selectmode=tk.SINGLE,
            selectbackground="#e3e3e3",
            selectforeground="#3B3B3B",
        )
        self._character_listbox.pack(side="top", expand=True, fill="both")

        self.__startMatchButton = tk.Button(
            self.frame,
            text="Start Game",
            bg="orange",
            fg="white",
            font=font.Font(weight="bold"),
            command=window.interface.send_match_settings,
        )
        # Pack the button at the bottom left
        self.__startMatchButton.pack(side=tk.RIGHT, anchor=tk.SW)

    def update_char_info(self, characters: dict[str : dict], initiative_queue: list[str] ):
        # Clear the listbox first
        self._character_listbox.delete(0, tk.END)

        # Add the characters to the listbox
        for name in initiative_queue:
            char = characters[name]
            upd_text = f"LV.{char['level']} {char['name']}, HP: {char['hp']}/{char['hp_max']} Initiative: {char['initiative']}"
            self._character_listbox.insert(tk.END, upd_text)
