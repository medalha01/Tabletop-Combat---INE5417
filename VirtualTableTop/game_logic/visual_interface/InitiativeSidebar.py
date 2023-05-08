from VirtualTableTop.game_logic.visual_interface.Widget import Widget
import tkinter as tk


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

    def update_char_info(self, character_list, speed_used="0.0"):
        # Clear the listbox first
        self._character_listbox.delete(0, tk.END)

        # Add the characters to the listbox
        for character in character_list:
            self._character_listbox.insert(tk.END, character.name)
