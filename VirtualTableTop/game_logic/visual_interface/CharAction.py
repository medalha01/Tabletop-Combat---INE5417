from VirtualTableTop.game_logic.visual_interface.Widget import Widget
import tkinter as tk
import random


class CharAction(Widget):
    def __init__(self, window) -> None:
        super().__init__(window)
        self._text = tk.Label(self.frame, text=f"Action {random.randint(0,100)}", font=("arial", 20))
        self._text.pack(side="top", anchor="w")
