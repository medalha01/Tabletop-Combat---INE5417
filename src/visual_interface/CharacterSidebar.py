

from Widget import Widget
from CharAction import CharAction
import tkinter as tk


class CharacterSidebar(Widget):
    def __init__(self, window) -> None:
        super().__init__(window)

        # Character Info

        self._character_info = tk.Frame(self.frame, bg="#3B3B3B", width=200, padx=10)
        self._character_info.pack(side="top")
        self._text_name = tk.Label(self._character_info, text="New Character", font=("helvetica", 30), bg="#3B3B3B", fg="#e3e3e3")
        self._text_att = tk.Label(self._character_info, text="Level: HP: Initiave: CA: Speed: ", 
                                  font=("helvetica", 16), wraplength=100, bg="#3B3B3B", fg="#e3e3e3", justify="left")
        self._text_name.pack(side="top")
        self._text_att.pack(side="top", anchor='w')

        #Actions Sidebar

        self._action_sidebar = tk.Canvas(self.frame, bg="#3B3B3B", scrollregion=(0,0,5000,5000))
        self._action_sidebar.pack(anchor='w', expand=True, fill="both")
        self._action_scrollbar = tk.Scrollbar(self._action_sidebar)
        self._action_scrollbar.pack(side="right", fill='y')

        self._action = tk.Frame(self._action_sidebar, bg="#3B3B3B")
        self._action_sidebar.create_window(0,0,window=self._action, anchor='nw')
        self._action_scrollbar.config(command=self._action_sidebar.yview)
        self._action_sidebar.config(yscrollcommand=self._action_scrollbar.set)

        self._action_list = [CharAction(self._action) for i in range (100)]
        for action in self._action_list:
            action.frame.pack(fill='x')
    
    def update_char_info(self, character, speed_used = '0.0'):
        self._text_name.configure(text=character.name)
        upd_text = f"Level: {character.level} HP: {character.hp} Initiave: {character.initiative} CA: {character.ca} Speed: {speed_used}]/{character.speed}"
        self._text_att.configure(text=upd_text)

        #...
