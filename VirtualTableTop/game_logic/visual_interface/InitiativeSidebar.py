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
            text="Start Match",
            bg="orange",
            fg="white",
            font=font.Font(weight="bold"),
            command=window.open_start_match,
        )
        # Pack the button at the bottom left
        self.__startMatchButton.pack(side=tk.RIGHT, anchor=tk.SW)

    def update_char_info(self, characters: dict[str : dict], initiative_queue: list[str] ):
        # Clear the listbox first
        self._character_listbox.delete(0, tk.END)
        initiative_queue.reverse()
        # Add the characters to the listbox
        for i, name in enumerate(initiative_queue):
            char = characters[name]
            upd_text = f"LV.{char['level']} {char['name']}, HP: {char['hp']}/{char['hp_max']} Initiative: {char['initiative']}"
            self._character_listbox.insert(tk.END, upd_text)
            self._character_listbox.itemconfig(i, {'fg': char['color']})


    def update_context_button(self, match_status: int):
        if match_status == 0:
            self.__startMatchButton.config(text="Start Match", command=self.window.open_start_match)
        elif match_status == 1:
            self.__startMatchButton.config(text="Configure Match", command=self.window.open_settings_window)
        elif match_status == 2:
            self.__startMatchButton.config(text="Calculate Initiative", command=self.window.interface.send_iniciative)
        elif match_status == 3:
            self.__startMatchButton.config(text="Skip Turn", command=self.window.interface.skip_turn)