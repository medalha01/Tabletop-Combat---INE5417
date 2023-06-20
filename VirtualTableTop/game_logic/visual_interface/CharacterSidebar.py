from VirtualTableTop.game_logic.visual_interface.Widget import Widget
from VirtualTableTop.game_logic.visual_interface.CharAction import CharAction
import tkinter as tk


class CharacterSidebar(Widget):
    def __init__(self, window) -> None:
        super().__init__(window)
        # Character Info
        self._action_list = []
        self._character_info = tk.Frame(self.frame, bg="#3B3B3B", width=300, padx=10, )
        self._character_info.pack(side="top")

        self._text_name = tk.Label(
        self._character_info,
        text="New Character",
        bg="#3B3B3B",
        fg="#e3e3e3",
        font=("helvetica", 20),        
        )
        self._text_att = tk.Label(
            self.frame,
            text="Level:\n HP: \nInitiave: \nCA: \nSpeed: ",
            font=("helvetica", 16),
            wraplength=300,
            bg="#3B3B3B",
            fg="#e3e3e3",
            justify="left",
        )
        self._text_name.pack(side="top")
        self._text_att.pack(side="top", anchor="w")

        # Actions Sidebar
        self._action_disselect_button = tk.Button(self.frame, text='Disselect Action', command=window.select_action)
        self._action_disselect_button.pack(anchor='n', fill='x')

        self._action_sidebar = tk.Canvas(
            self.frame, bg="#3B3B3B", scrollregion=(0, 0, 1000, 1000)
        )
        self._action_sidebar.pack(anchor="w", expand=True, fill="both")
        self._action_scrollbar = tk.Scrollbar(self._action_sidebar,)
        self._action_scrollbar.pack(side="right", fill="y")

        self._action = tk.Frame(self._action_sidebar, bg="#3B3B3B")
        self._action_sidebar.create_window(0, 0, window=self._action, anchor="nw")
        self._action_scrollbar.config(command=self._action_sidebar.yview)
        self._action_sidebar.config(yscrollcommand=self._action_scrollbar.set)

    def update_action_list(self, actions):
        for action in self._action_list:
            action.pack_forget()
        self._action_list = []
        for action in actions:
            text = f"{action['name']} {action['times_used']}/{action['max_amount']}\n{len(action['dices'])}d{action['dices'][0]}\nRoll:{action['roll_bonus']}\nEffect:{action['dmg_bonus']}\nRange:{action['range']}\nAoe:{action['aoe_radius']}"
            action_widget = tk.Label(self._action, text= text, font=("arial", 14), bg="#3B3B3B",
                                     fg="#e3e3e3",highlightcolor="#e3e3e3", highlightthickness=1)
            action_widget.bind("<Button-1>", lambda event, action=action['name']: self.window.select_action(action))
            action_widget.pack(anchor='nw', fill='x')
            self._action_list.append(action_widget)

    def update_char_info(self, character: dict):
        self._text_name.configure(text=character['name'])
        upd_text = f"Level: {character['level']} \nHP: {character['hp']}/{character['hp_max']} \nInitiave: {character['initiative']} \nCA: {character['ca']} \nSpeed: {character['moved_amount']}/{character['speed']}"
        self._text_att.configure(text=upd_text)

        # ...
